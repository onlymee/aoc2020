import Data.List.Split (splitOn)
import qualified Data.Map.Strict as M

parseRule :: String -> [(Int,[[Int]])]   -- M.Map Int [[Int]]
parseRule txt = do
    let (rulelabel:def:rest) = splitOn ": " txt
    let rule = read rulelabel :: Int
    alt <- map (\x-> map read $ splitOn " " x) $ splitOn " | " def
    [(rule,alt)]


main :: IO()
main = do
    input <- readFile "day19/input.txt"
    let [ruleinput,messages] = splitOn [""] $ lines input

    let rules=map parseRule ruleinput
    print rules
    -- print  $ evaluate $ fromJust $ parseTest (pExpr <* eof) "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    let answer1= -1
    let answer2= -1
    print (answer1, answer2)