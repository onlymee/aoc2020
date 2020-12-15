--import System.IO
--import Data.List (take,elemIndex)
import qualified Data.IntMap.Strict as M
--import Data.Maybe (fromJust)
 
play :: (M.Key, M.Key, M.IntMap M.Key) -> (M.Key, M.Key, M.IntMap M.Key)
play (lastspoken,lastturn,spoken) = case M.lookup lastspoken spoken of 
                                    Just y  -> (lastturn-y,lastturn+1,M.insert lastspoken lastturn spoken)
                                    Nothing -> (0         ,lastturn+1,M.insert lastspoken lastturn spoken)

geti i (lastspoken, lastturn, spoken)
    | lastturn==i = lastspoken
    | otherwise   = geti i $ play (lastspoken, lastturn, spoken)


main = do
    let spoken = M.fromList $ zip [0,14,1,3,7] [1..]
    let start = (9,6, spoken) 
    print spoken
    print $ geti 2020 start
    print $ geti 30000000 start

    