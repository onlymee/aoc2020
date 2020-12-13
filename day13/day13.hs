import System.IO
import Data.List.Split (splitOn)

eeuclid :: Integral c => c -> c -> (c, c, c)
eeuclid 0 b = (b, 0, 1)
eeuclid a b = (g, t - (b `div` a) * s, s)
    where (g, s, t) = eeuclid (b `mod` a) a


modinv :: Integral a => a -> a -> a
modinv a m = let (_, i, _) = eeuclid a m in i `mod` m

crt :: [(Integer, Integer)] -> Integer
crt rms = fst $ foldr iter (0, 1) rms
    where
    iter (r1, m1) (r2, m2) = (r `mod` m, m)
        where r = r2 + m2 * (r1 - r2) * (m2 `modinv` m1)
              m = m2 * m1


readBuses :: Integer -> [String] -> [(Integer, Integer)]
readBuses i [] = []
readBuses i (b:bs) = case b of
    "x" -> readBuses (i+1) bs
    _   -> ((bi-i) `mod` bi,bi):readBuses (i+1) bs
    where bi = read b :: Integer

modAny :: [(Integer,Integer)] -> Integer -> (Integer,Integer)
modAny [] _ = (0,0)
modAny (b:bs) x 
  |  x `mod` m == 0 = (x, m)
  |  otherwise        = modAny bs x
    where
        (_,m)=b


main :: IO()
main = do
    --let test1=[(0,7),(12,13),(55,59),(25,31),(12,19)]
    --print $ crt test1
    input <- readFile "day13/input.txt"
    let lns = lines input
    let part1 = read (head lns) :: Integer
    let buses = readBuses 0 $ splitOn "," (lns !! 1)
    let earliest = head $ filter (/= (0,0)) $ map (modAny buses) [part1..]

    let answer1 = (\(x,b) -> (x-part1)*b) earliest
    let answer2 = crt buses

    print (answer1, answer2)
    

    