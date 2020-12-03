import System.IO

goSlide :: [String] -> (Int, Int) -> Int -> Int -> Int
goSlide [] _ _ trees = trees
goSlide hill (dx, dy) pos trees = goSlide (drop dy hill) (dx, dy) (pos+dx) (trees+tree)
    where 
        here = row !! (pos `mod` length row)
        row = head hill
        tree 
            | here == '#' = 1
            | otherwise   = 0


toboggan :: [String] -> (Int, Int) -> Int
toboggan hill (dx, dy) = goSlide (drop dy hill) (dx, dy) dx 0 

main = do
    input <- readFile "day3/input.txt"
    let hill = lines input
    print $ toboggan hill (3, 1)
    print $ product $ map (toboggan hill) [(1,1),(3,1),(5,1),(7,1),(1,2)]