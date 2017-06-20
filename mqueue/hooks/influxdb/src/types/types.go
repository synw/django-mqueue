package types

import (
	"time"
)

type Event struct {
	Id          string    `gorm:"primary_key"`
	Name        string    `gorm:"column:name"`
	Class       string    `gorm:"column:class"`
	ContentType string    `gorm:"column:content_type"`
	ObjPk       int       `gorm:"column:pk"`
	User        string    `gorm:"column:user"`
	Url         string    `gorm:"column:url"`
	AdminUrl    string    `gorm:"column:admin_url"`
	Notes       string    `gorm:"column:notes"`
	Request     string    `gorm:"column:request"`
	Domain      string    `gorm:"column:domain"`
	Date        time.Time `gorm:"column:date"`
}

type Db struct {
	Addr string
	User string
	Pwd  string
	Name string
}
