let LIVE_0 = 0
let LIVE_1 = 2

document.addEventListener("DOMContentLoaded", () => {
    const textInput = document.getElementById("input")
    const hashOutput = document.getElementById("hash")
    const hashTenOutput = document.getElementById("hash-base-10")

    const copyButton = document.getElementById("copy")
    const copyToolTip = document.getElementById("copy-tooltip")

    const generateButton = document.getElementById("generate")
    const generateIcon = document.getElementById("generate-icon")

    const rangeSliderZero = document.getElementById("range-slider-zero")
    const rangeSliderOne = document.getElementById("range-slider-one")
    const rangeInputZero = document.getElementById("range-input-zero")
    const rangeInputOne = document.getElementById("range-input-one")
   
    copyButton.addEventListener("click", () => {
        textInput.select()
        document.execCommand("copy")

        copyToolTip.innerText = `Copied: ${textInput.value.length > 10 ? textInput.value.substring(0, 7) + "..." : textInput.value}`
    })

    textInput.addEventListener("keypress", (event) => {
        if (event.key == "Enter") {
            fetch("/hash", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: textInput.value,
                    live_0: LIVE_0,
                    live_1: LIVE_1
                })
            }).then((res) => {
                return res.json()
            }).then((data) => {
                hashOutput.value = data.hex
                hashTenOutput.innerText = `Base 10: ${data.dec}`
            }).catch((error) => {
                console.log(error)
            })
        }
    })

    copyButton.addEventListener("mouseenter", () => {
        copyToolTip.innerText = "Copy to Clipboard"
    })

    generateButton.addEventListener("click", () => {
        if (generateIcon.classList.contains("rotate-first-half")) {
            generateIcon.classList.remove("rotate-first-half")
            generateIcon.classList.add("rotate-second-half")
        } else {
            generateIcon.classList.remove("rotate-second-half")
            generateIcon.classList.add("rotate-first-half")
        }
        console.log(textInput.value)
        fetch("/hash", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: textInput.value,
                live_0: LIVE_0,
                live_1: LIVE_1
            })
        }).then((res) => {
            return res.json()
        }).then((data) => {
            hashOutput.value = data.hex
            hashTenOutput.innerText = `Base 10: ${data.dec}`
        }).catch((error) => {
            console.log(error)
        })
    })

    rangeSliderZero.addEventListener("input", event => {
        LIVE_0 = +event.target.value
        rangeInputZero.value = LIVE_0
    })

    rangeSliderOne.addEventListener("input", event => {
        LIVE_1 = event.target.value
        rangeInputOne.value = LIVE_1
    })

    rangeInputZero.addEventListener("keypress", event => {
        if (event.key === "Enter") {
            const value = Math.round(event.target.value)
            if (value < 0) {
                LIVE_0 = 0
            } else if (value > 4) {
                LIVE_0 = 4
            } else {
                LIVE_0 = value
            }
            rangeInputZero.value = LIVE_0
            rangeSliderZero.value = LIVE_0
        }
    })

    rangeInputOne.addEventListener("keypress", event => {
        if (event.key === "Enter") {
            const value = Math.round(event.target.value)
            if (value < 0) {
                LIVE_1 = 0
            } else if (value > 4) {
                LIVE_1 = 4
            } else {
                LIVE_1 = value
            }
            rangeInputOne.value = LIVE_1
            rangeSliderOne.value = LIVE_1
        }
    })
})
