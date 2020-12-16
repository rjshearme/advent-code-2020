import Data.List
import Data.List.Split
import System.Environment

count :: Int -> [Int] -> Int
count n [] = 0
count n (x:xs)  | (x == n) = 1 + count n xs
                | otherwise = count n xs


solvePart1 :: String -> IO Int
solvePart1 inputString = do
    let adapterList = splitOn "\n" inputString
    let adapterListSorted = [0] ++ (sort $ map(read::String->Int) adapterList)
    let differences = zipWith (-) (tail adapterListSorted) adapterListSorted
    let volt3Differences = count 3 differences + 1
    let volt1Differences = count 1 differences
    print(volt1Differences * volt3Differences)
    return 1


main = do
    args <- getArgs
    inputData <- readFile $ head args
    solution <- if args !! 1 == "1" then (solvePart1 inputData) else (solvePart2 inputData)
    print(solution)