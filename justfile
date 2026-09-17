#!/usr/bin/env -S just --justfile


set default-list := true
[windows]
set shell := ["powershell.exe", "-NoLogo", "-Command"]


cargo-invocation := 'cargo +nightly -Z unstable-options -C plugin'
[windows]
cargo-xwin-invocation := cargo-invocation
[unix]
cargo-xwin-invocation := cargo-invocation + ' xwin'


[no-exit-message]
cargo *args:
    {{cargo-invocation}} {{args}}

build-arch arch *args:
    {{cargo-xwin-invocation}} build -Z unstable-options --target {{arch}}-pc-windows-msvc --artifact-dir ../apworld/mushroom_age/randomushroom/files/plugin/{{arch}} {{args}}
    -rm apworld/mushroom_age/randomushroom/files/plugin/{{arch}}/randomushroom.asi
    mv apworld/mushroom_age/randomushroom/files/plugin/{{arch}}/randomushroom.dll apworld/mushroom_age/randomushroom/files/plugin/{{arch}}/randomushroom.asi

build *args: (build-arch 'i686' args) (build-arch 'x86_64' args)
