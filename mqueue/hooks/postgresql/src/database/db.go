package database

import (
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"github.com/synw/mqueue-pg/types"
	"github.com/synw/terr"
)

func Save(db *types.Db, event types.Event) *terr.Trace {
	conn := "host=" + db.Addr + " user=" + db.User + " dbname=" + db.Name + " sslmode=disable password=" + db.Pwd + ""
	gdb, err := gorm.Open("postgres", conn)
	if err != nil {
		tr := terr.New("db.postgresql.connect()", err)
		return tr
	}
	defer gdb.Close()
	gdb.NewRecord(event)
	gdb.Create(&event)
	return nil
}

func Migrate(db *types.Db) *terr.Trace {
	conn := "host=" + db.Addr + " user=" + db.User + " dbname=" + db.Name + " sslmode=disable password=" + db.Pwd + ""
	gdb, err := gorm.Open("postgres", conn)
	if err != nil {
		tr := terr.New("db.postgresql.connect()", err)
		return tr
	}
	defer gdb.Close()
	gdb.AutoMigrate(&types.Event{})
	fmt.Println("Database " + db.Name + " has been successfully migrated")
	return nil
}
