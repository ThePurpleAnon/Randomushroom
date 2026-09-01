#!/usr/bin/env -S just --justfile


[windows]
set shell := ["powershell.exe", "-NoLogo", "-Command"]


cargo-invocation := 'cargo +nightly -Z unstable-options -C plugin'


default:
    just --list

[no-exit-message]
cargo *args:
    {{cargo-invocation}} {{args}}

build *args:
    {{cargo-invocation}} build --target i686-pc-windows-msvc --artifact-dir ../randomushroom/files/plugin {{args}}
    -rm randomushroom/files/plugin/randomushroom.asi
    mv randomushroom/files/plugin/randomushroom.dll randomushroom/files/plugin/randomushroom.asi

run *args: build
    poetry run python -m randomushroom {{args}}
