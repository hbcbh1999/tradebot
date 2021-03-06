/*
 * File: tradebot.go
 * ------------------------------
 * Tradebot
 */

package main

import (
    "fmt"
    "encoding/json"
    "io"
    "log"
    "strings"
    "net"
)

type ClientMessage struct {
    Type string
    Team string
    Order_Id int
    Symbol string
    Dir string
}

type ServerMessage struct {
    Type string
    Symbol string

}

func handleConnection(c net.Conn) {
    d : json.NewDecoder(c)

}

func listen() {
    ln, err := net.Listen("tcp", "test-exch-SEGFAULT:2000")
    if err != nil {
        fmt.Println("  couldn't connect, retrying")
        fmt.Println(err)
        return
    }    
    for {
        // accept connection
        connection, err := ln.Accept()
        if err != nil {
            fmt.Println(err)
            continue
        }
        // handle connection
        go handleServerConnection(connection)
    }
}

func connectToServer() {
    for {
        fmt.Println("  connecting to server...")
        listen()
    }
}

func main() {
    fmt.Println("tradebot starting up...")
    connectToServer()
}