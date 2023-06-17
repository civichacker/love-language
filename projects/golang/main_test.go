package main

import (
    "testing"
    "encoding/json"
    "fmt"
)

func TestSchemaLoading(t *testing.T){
    var tests = []struct {
            name string
            filename string
        }{
            // the table itself
            {"use of force", "schemas/use-of-force.schema"},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            content, err := schemas.ReadFile(fmt.Sprintf("%s.json", tt.filename))
            result := json.Valid([]byte(content))

            if err != nil {
             t.Errorf("loading schema failed: %s", err)
            } else if !result {
             t.Errorf("schema is not valid JSON")
            }
        })
    }
}
