const levelToRgb = (level) => {
    let q = (256 / level).toFixed(0).toString(16).repeat(3)
    console.log(level, q)
    return q
}

export default levelToRgb
