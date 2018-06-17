def Pack(event):
    sep = "#!#"
    data = ["name:;" + event.name]
    if event.event_class:
        data.append("event_class:;" + event.event_class)
    if event.content_type:
        data.append("content_type:;" + str(event.content_type))
    if event.obj_pk:
        data.append("obj_pk:;" + str(event.obj_pk))
    if event.user:
        data.append("user:;" + str(event.user))
    if event.url:
        data.append("url:;" + event.url)
    if event.admin_url:
        data.append("admin_url:;" + event.admin_url)
    if event.notes:
        data.append("notes:;" + str(event.notes))
    if event.request:
        request = event.request.replace("\n", "//")
        data.append("request:;" + request)
    if event.bucket:
        data.append("bucket:;" + event.bucket)
    if event.data or event.data != {}:
        data.append("data:;" + str(event.data))
    d = str.join(sep, data)
    return d
