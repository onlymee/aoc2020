{-# LANGUAGE OverloadedStrings #-} 
import Prelude hiding (readFile, lines)
import Data.Text.IO 
import Control.Applicative (empty) 
import Control.Monad (void)
import Text.Megaparsec
    ( parseMaybe,
      between,
      choice,
      Parsec,
      MonadParsec(eof) )
import Text.Megaparsec.Char ( space1 )
import qualified Text.Megaparsec.Char.Lexer as L
import Data.Text (Text, lines)
import Data.Void ( Void )
import Data.Maybe ( fromJust )
import Control.Monad.Combinators.Expr

type Parser = Parsec Void Text

data Expr
  = Int Int
  | Sum      Expr Expr
  | Product  Expr Expr
  deriving (Eq, Ord, Show)

sc :: Parser ()
sc = L.space (void space1) empty empty

lexeme :: Parser a -> Parser a
lexeme = L.lexeme sc

operatorTable :: [[Operator Parser Expr]]
operatorTable =
  [ [ binary "*" Product
      , binary "+" Sum
    ]
  ]

operatorTable2 :: [[Operator Parser Expr]]
operatorTable2 =
  [ [   binary "+" Sum
    ]
  , [   binary "*" Product
    ]
  ]

symbol :: Text -> Parser Text
symbol = L.symbol sc

binary :: Text -> (Expr -> Expr -> Expr) -> Operator Parser Expr
binary  name f = InfixL  (f <$ symbol name)

pInteger :: Parser Expr
pInteger = Int <$> lexeme L.decimal

parens :: Parser a -> Parser a
parens = between (symbol "(") (symbol ")")

-- Answer 1
pExpr :: Parser Expr
pExpr = makeExprParser pTerm operatorTable

pTerm :: Parser Expr
pTerm = choice
  [ parens pExpr
  , pInteger
  ]

-- Answer 2
pTerm2 :: Parser Expr
pTerm2 = choice
  [ parens pExpr2
  , pInteger
  ]

pExpr2 :: Parser Expr
pExpr2 = makeExprParser pTerm2 operatorTable2

evaluate :: Expr -> Int
evaluate (Sum a b) = evaluate a + evaluate b
evaluate (Product a b) = evaluate a * evaluate b
evaluate (Int a) = a

main :: IO()
main = do
    input <- readFile "day18/input.txt"
    let lns=lines input
    let exprs =  map (parseMaybe (pExpr <* eof)) lns
    let answer1 = sum $ map (evaluate.fromJust) exprs

    let exprs2 = map (parseMaybe (pExpr2 <* eof)) lns
    let answer2 = sum $ map (evaluate.fromJust) exprs2
  
    -- print  $ evaluate $ fromJust $ parseTest (pExpr <* eof) "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    print (answer1, answer2)