import System.IO
import Data.List (take,elemIndex)
import Data.List.Split (splitOn)
import Data.Maybe (fromJust)

canMake :: (Eq a, Num a) => a -> [a] -> [a] -> Bool
canMake n ds (c:cs) = (n-c) `elem` (ds ++ (c:cs)) || canMake n (c:ds) cs
canMake _ _ [] = False

scanForBreak :: (Eq a, Num a, Ord a) => [a] -> Maybe a
scanForBreak (a:as) 
    | length list /= 26   = Nothing
    | canMake n [] from   = scanForBreak as
    | otherwise           = Just n
    where list = take 26 (a:as)
          from = take 25 list
          n=last list

findSeq :: (Eq a, Num a, Ord a) => a -> [a] -> Maybe [a]
findSeq n (c:cs) = case idx of
                    Nothing -> findSeq n cs
                    Just i -> Just $ take i (c:cs)
            where idx = elemIndex n ((drop 1 . scanl1 (+)) (c:cs))
findSeq _ [] = Nothing
  

main = do
    handle <- openFile "day9/input.txt" ReadMode
    input <- hGetContents handle
    let code = map read $ words input
    let answer1 = fromJust (scanForBreak code)
    let seq =  fromJust (findSeq answer1 code)
    let answer2 = maximum seq + minimum seq
    print (answer1, answer2)

    