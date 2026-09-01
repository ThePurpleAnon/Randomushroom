use std::{
    backtrace::Backtrace,
    panic::{self, PanicHookInfo},
};

use winsafe::{self as w, co, prelude::*};

fn panic_hook(info: &PanicHookInfo) {
    let backtrace = Backtrace::force_capture();
    let _ = w::HWND::NULL.MessageBox(
        &format!(
            "\
Error in the Randomushroom plugin!

{info}

stack backtrace:
{backtrace}"
        ),
        "Error in the Randomushroom plugin!",
        co::MB::ICONERROR,
    );
}

#[dllmain_rs::entry]
fn on_process_attach() {
    panic::set_hook(Box::new(panic_hook));

    w::HWND::NULL
        .MessageBox(
            "Hello from the Randomushroom plugin!",
            "Hello!",
            co::MB::ICONINFORMATION,
        )
        .unwrap();
}
