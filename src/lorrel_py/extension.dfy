module Lorrel {
    import Math = Std.Math

    function MinMax(x: int, y: int) : (int, int)
    {
        (Math.Min(x, y), Math.Max(x, y))
    }

    const Min := Math.Min
    const Max := Math.Max
}