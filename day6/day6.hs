import System.IO
import qualified Data.Map.Strict as M
import Data.List (intersect,drop,findIndex,unzip,sort)
import Data.List.Split (splitOn)
import Text.Regex.Posix

elimDupes [] acc = acc                          -- empty
elimDupes (x:xs) acc                    
        | elem x acc = elimDupes xs acc         -- head in acc
        | otherwise = elimDupes xs (acc ++ [x]) -- head not in acc
compress :: String -> String
compress l = elimDupes l [] 

intersectAll :: [String] -> String -> String
intersectAll [] acc = acc
intersectAll (l:ls) acc = intersectAll ls (intersect acc l)

main = do
    input <- readFile "day6/input.txt"
    let answer1 =  map length $ map compress $ map (filter (\x ->  x/='\n')) $ map sort $ splitOn "\n\n" $ input
    print (sum answer1)
    let answer2 =  map length $ map (\x -> intersectAll x  "abcdefghijklmnopqrstuvwxyz") $ map lines $ splitOn "\n\n" $ input
    print (sum answer2)

    