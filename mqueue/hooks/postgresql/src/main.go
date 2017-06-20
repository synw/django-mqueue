package main

import (
	"errors"
	"flag"
	"github.com/SKAhack/go-shortid"
	"github.com/synw/mqueue-pg/database"
	"github.com/synw/mqueue-pg/types"
	"github.com/synw/terr"
	"time"
)

var migrate = flag.Bool("m", false, "Migrate database")
var addr = flag.String("a", "", "Database address")
var db = flag.String("d", "", "Database")
var table = flag.String("t", "", "Table")
var dbuser = flag.String("du", "", "Database user")
var pwd = flag.String("p", "", "Database password")
var name = flag.String("n", "", "Name")
var class = flag.String("c", "", "Class")
var contentType = flag.String("ct", "", "Content type")
var objPk = flag.Int("o", 0, "Object primary key")
var user = flag.String("u", "", "User")
var url = flag.String("ur", "", "Url")
var adminUrl = flag.String("au", "", "Admin url")
var notes = flag.String("no", "", "Notes")
var request = flag.String("r", "", "Request")
var g = shortid.Generator()

func main() {
	flag.Parse()
	//terr.Debug(*addr, *db, *table, *dbuser, *pwd, *name, *class, *contentType, *objPk, *user, *url, *adminUrl, *notes, *request)

	// verify flags
	var tr *terr.Trace
	if *addr == "" {
		err := errors.New("No database address")
		terr.Add("main", err, tr)
	}
	if *db == "" {
		err := errors.New("No database")
		terr.Add("main", err, tr)
	}
	if *table == "" {
		err := errors.New("No database table")
		terr.Add("main", err, tr)
	}
	if *dbuser == "" {
		err := errors.New("No database user")
		terr.Add("main", err, tr)
	}
	if *pwd == "" {
		err := errors.New("No database password")
		terr.Add("main", err, tr)
	}
	// init db obj
	dbObj := &types.Db{
		*addr,
		*dbuser,
		*pwd,
		*db,
		*table,
	}
	// migration option
	if *migrate == true {
		tr := database.Migrate(dbObj)
		if tr != nil {
			tr.Fatal("main")
		}
		return
	}
	// fire event
	now := time.Now()
	event := types.Event{
		g.Generate(),
		*name,
		*class,
		*contentType,
		*objPk,
		*user,
		*url,
		*adminUrl,
		*notes,
		*request,
		now,
	}
	tr = database.Save(dbObj, event)
	if tr != nil {
		tr.Fatal("main")
	}
}
