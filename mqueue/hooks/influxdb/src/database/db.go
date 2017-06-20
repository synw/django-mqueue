package database

import (
	"github.com/influxdata/influxdb/client/v2"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"github.com/synw/mqueue-influx/types"
	"github.com/synw/terr"
	"strconv"
	"time"
)

func Save(db *types.Db, event types.Event) *terr.Trace {
	// init
	cli, err := client.NewHTTPClient(client.HTTPConfig{
		Addr:     db.Addr,
		Username: db.User,
		Password: db.Pwd,
	})
	if err != nil {
		tr := terr.New("db.Save", err)
		return tr
	}
	// record
	bp, err := client.NewBatchPoints(client.BatchPointsConfig{
		Database:  db.Name,
		Precision: "s",
	})
	if err != nil {
		tr := terr.New("db.influxdb.Save", err)
		return tr
	}
	tags := map[string]string{
		"service":      "mqueue_events",
		"domain":       event.Domain,
		"class":        event.Class,
		"content_type": event.ContentType,
		"object_pk":    strconv.Itoa(event.ObjPk),
		"user":         event.User,
		"url":          event.Url,
		"admin_url":    event.AdminUrl,
		"name":         event.Name,
	}
	fields := map[string]interface{}{
		"num": 1,
	}
	pt, err := client.NewPoint("event", tags, fields, time.Now())
	if err != nil {
		tr := terr.New("db.Save", err)
		return tr
	}
	bp.AddPoint(pt)
	// Write the batch
	if err := cli.Write(bp); err != nil {
		tr := terr.New("db.Save", err)
		return tr
	}
	return nil
}
