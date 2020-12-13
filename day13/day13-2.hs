import System.IO

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

getInput :: Integral b => (b, b) -> (b, b)
getInput (a,b) = ((b-a) `mod` b,b)

main :: IO()
main = do
      let b=[29,41,37,653,13,17,23,823,19]
      let d=[0,19,23,29,42,46,52,60,79]
--    let b=[7,13,59,31,19]
--    let d=[0,1,4,6,7]
      let result = crt $ map getInput $ (zip d b)
      print(result)
    --let cfs = concatMap (getCF busmap) (pairs b)
    --print $ foldl1 (lcm) cfs
    --print $ foldl1 (lcm) b
    --print $ map (\(x,y) -> lcm x y) $ pairs b
    --print $ pairs b

    

    