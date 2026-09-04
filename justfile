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
    -rm randomushroom/files/plugin/randomushroom32.asi
    mv randomushroom/files/plugin/randomushroom.dll randomushroom/files/plugin/randomushroom32.asi
    -rm randomushroom/files/plugin/randomushroom32.pdb
    mv randomushroom/files/plugin/randomushroom.pdb randomushroom/files/plugin/randomushroom32.pdb
    -rm randomushroom/files/plugin/randomushroom32.dll.lib
    mv randomushroom/files/plugin/randomushroom.dll.lib randomushroom/files/plugin/randomushroom32.dll.lib

    {{cargo-invocation}} build --target x86_64-pc-windows-msvc --artifact-dir ../randomushroom/files/plugin {{args}}
    -rm randomushroom/files/plugin/randomushroom64.asi
    mv randomushroom/files/plugin/randomushroom.dll randomushroom/files/plugin/randomushroom64.asi
    -rm randomushroom/files/plugin/randomushroom64.pdb
    mv randomushroom/files/plugin/randomushroom.pdb randomushroom/files/plugin/randomushroom64.pdb
    -rm randomushroom/files/plugin/randomushroom64.dll.lib
    mv randomushroom/files/plugin/randomushroom.dll.lib randomushroom/files/plugin/randomushroom64.dll.lib

run *args: build
    poetry run python -m randomushroom {{args}}
