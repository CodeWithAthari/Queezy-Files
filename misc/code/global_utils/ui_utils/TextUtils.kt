package com.devatrii.queezy.global_utils.ui_utils


fun Int.beautifyIntAsString(): String {
    return if (this < 10)
        "0$this"
    else
        this.toString()
}