import Data.List.Split
import qualified Data.Map as Map
import qualified Data.Set as Set
import System.Environment

solvePart1 :: String -> IO Int
solvePart1 inputString = do
  return $ countCustomsDeclarationsPart1 (splitOn "\n\n" inputString)


countCustomsDeclarationsPart1 :: [[Char]] -> Int
countCustomsDeclarationsPart1 groupStrings = sum $ map numberOfUniqueDeclarations groupStrings

solvePart2 :: String -> IO Int
solvePart2 inputString = do
  return $ sum $ map countCustomsDeclarationsPart2 (splitOn "\n\n" inputString)

countCustomsDeclarationsPart2 :: [Char] -> Int
countCustomsDeclarationsPart2 groupString = length $ Map.filter (==(numberOfPeopleDeclaring groupString)) (frequencyOfDeclarations groupString)

frequencyOfDeclarations :: (Ord a) => [a] -> Map.Map a Integer
frequencyOfDeclarations xs = Map.fromListWith (+) [(x, 1) | x <- xs]

numberOfUniqueDeclarations :: String -> Int
numberOfUniqueDeclarations declaration = length $ Set.filter (/="") $ Set.filter (/="\n") $ Set.fromList (splitOn ""  declaration)

numberOfPeopleDeclaring :: String -> Integer
numberOfPeopleDeclaring declaration = toInteger $ length $ splitOn "\n" declaration


main = do
    args <- getArgs
    inputData <- readFile $ head args
    solution <- if args !! 1 == "1" then (solvePart1 inputData) else (solvePart2 inputData)
    print(solution)