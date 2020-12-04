import System.IO
import qualified Data.Map.Strict as M
import Data.List (intersect,drop,findIndex,unzip)
import Data.List.Split (splitOn)
import Text.Regex.Posix

type Passport = [(String, String)]

readPassport s = map readField s

readField :: String -> (String,String)
readField cs = (label, drop 1 value)
    where (label, value) = case (findIndex (== ':') cs) of
                             Just x  -> splitAt x cs
                             Nothing -> ([],[':'] ++ cs)


requiredKeys=["byr","ecl","eyr","hcl","hgt","iyr","pid"] 

validPassport1 :: Passport -> Bool
validPassport1 passport = requiredKeys == intersect requiredKeys keys
   where (keys,values) = unzip passport


validateField :: (String, String) -> Bool
validateField (key,value)
     | key == "byr" = value =~ "^19[2-9][0-9]|200[0-2]$"
     | key == "iyr" = value =~ "^201[0-9]|2020$"
     | key == "eyr" = value =~ "^202[0-9]|2030$"
     | key == "hgt" = value =~ "^(59|6[0-9]|7[0-6])in$" || value =~ "^(1[5-8][0-9]|19[0-3])cm$" 
     | key == "hcl" = value =~ "^#[0-9a-f]{6}$"
     | key == "ecl" = value =~ "^amb|blu|brn|gry|grn|hzl|oth$"
     | key == "pid" = value =~ "^[0-9]{9}$"
     | otherwise = False

validPassport2 :: Passport -> Bool
validPassport2 passport = validPassport1 cleanedPassport
   where cleanedPassport = filter validateField passport


main = do
    input <- readFile "input.txt"
    let passports =  map readPassport $ map words $ splitOn "\n\n" $ input
    print $ length passports
    print $ length $ filter validPassport1 $ passports
    print $ length $ filter validPassport2 $ passports

    