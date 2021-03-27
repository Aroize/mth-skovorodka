const levelToRgb = (lvl) => {
    if (lvl === 0)
    return "a9a9a9"
    if (lvl===1)
     return "FB91A8"
    if (lvl===2)
     return "FB6B8A"
    if (lvl===3)
     return "F83A63"
    if (lvl===4)
     return "A11331"
    if (lvl===5)
     return "FFB994"
    if (lvl===6)
     return "FFA06D"
    if (lvl===7)
     return "FF803C"
    if (lvl===8)
     return "A64613"
    if (lvl===9)
     return "92BDEE"
    if (lvl===10)
     return "70ACEE"
    if (lvl===11)
     return "418BDD"
    if (lvl===12)
     return "154F90"
}

export default levelToRgb
