import System.IO

b2d :: [Char] -> Int
b2d s = helper $ reverse s
    where 
        helper [] = 0
        helper (c:cs)
            | c `elem` "BR" = 1 + 2 * (helper cs)
            | otherwise     = 2 * (helper cs)

seqsum :: (Int, Int) -> Int
seqsum (a,b) = (a+b)*(b-a+1) `div` 2

main = do
    input <- readFile "day5/input.txt"
    let seats = map b2d $ lines $ input
    print [b2d("BFFFBBFRRR"),567]
    print [b2d("FFFBBBFRRR"),119]
    print [b2d("BBFFBBFRLL"),820]
    let range = (minimum seats, maximum seats)
    let mySeat = (seqsum range) - sum seats
    print (range, mySeat)
