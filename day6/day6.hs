import System.IO
import Data.List (intersect,sort)
import Data.List.Split (splitOn)
import Data.String.Utils (strip)
import Data.List.Utils (uniq)

main = do
    input <- readFile "day6/input.txt"
    let records = splitOn "\n\n" $ input
    let answer1 =  map (length . sort . (filter (`elem` ['a'..'z'])). uniq) records
    let answer2 =  map (length . (foldr intersect ['a'..'z']) . lines) records
    print (sum answer1, sum answer2)

    