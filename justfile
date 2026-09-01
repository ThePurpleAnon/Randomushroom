#!/usr/bin/env -S just --justfile


cargo-invocation := 'cargo +nightly -Z unstable-options -C plugin'


default:
    just --list

[no-exit-message]
cargo *args:
    {{cargo-invocation}} {{args}}

build *args:
    {{cargo-invocation}} build --target i686-pc-windows-msvc --artifact-dir ../randomushroom/files {{args}}
    rm -f randomushroom/files/randomushroom.asi
    mv randomushroom/files/randomushroom.dll randomushroom/files/randomushroom.asi

run *args: build
    poetry run python -m randomushroom {{args}}
