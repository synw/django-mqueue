from typing import Any, Dict
from fastmcp import FastMCP
from pydantic import Field
from django.core.exceptions import PermissionDenied
from mcpx.auth import mcp_auth
from mqueue.models import MEvent
from mqueue.utils import formatEvent, validate_and_parse_date

name = "Mqueue Mcp Server"
mcp = FastMCP(name=name)


@mcp.tool()
async def query_events_since(
    start_date: str = Field(
        description="The start date for the query (use a standard Python date string)"
    ),
) -> Dict[str, Any]:
    """Query for events in the database since a given date"""
    try:
        mcp_auth()
    except PermissionDenied as e:
        print(f"Mcp authentication error: {e}")
        return {"error": "undefined"}
    parsed_date = validate_and_parse_date(start_date)
    results = []
    async for row in MEvent.objects.select_related("user").filter(
        date_posted__date__gte=parsed_date
    ):
        results.append(formatEvent(row))
    return {"result": results}


@mcp.tool()
async def query_events(
    nevents: int = Field(description="Maximum number of events to retrieve"),
) -> Dict[str, Any]:
    """Query for events in the database"""
    try:
        mcp_auth()
    except PermissionDenied as e:
        print(f"Mcp authentication error: {e}")
        return {"error": "undefined"}
    results = []
    async for row in MEvent.objects.select_related("user").all()[:nevents]:
        results.append(formatEvent(row))
    return {"result": results}


mcp_server = {
    "name": name,
    "mcp": mcp,
}
