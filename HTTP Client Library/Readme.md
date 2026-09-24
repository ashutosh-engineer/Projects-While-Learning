# HTTP Client Library

A lightweight HTTP client library built from scratch in Python to understand how web communication works at a low level.

## About the Project

This is my first learning project, focused on building an HTTP client without relying on high-level networking libraries. It uses raw TCP sockets to send and receive data, while keeping the code clean, readable, and object-oriented.

## What I Built

- TCP `send` and `sendall` functionality from scratch
- String-to-byte conversion for network communication
- HTTP request and response handling
- Status code and response inspection
- Object-oriented project structure
- Clean and understandable codebase

## Features

- `GET` requests
- `POST` requests
- `PUT` requests
- `DELETE` requests
- `OPTIONS` requests
- Custom headers
- Terminal-based login system
- Login implementation using built-in data structures only
- Request and activity history logs

## Goal

The goal is to create a simple, practical HTTP client library that allows users to send requests and clearly view the server's status codes and responses—without hiding the underlying network concepts behind high-level abstractions.