{-# LANGUAGE DuplicateRecordFields, FlexibleInstances, UndecidableInstances #-}

module Main where

import Control.Monad
import Data.Array
import Data.Bits
import Data.List
import Data.List.Split
import Data.Set
import Data.Text
import Debug.Trace
import System.Environment
import System.IO
import System.IO.Unsafe

--
-- Complete the 'simpleArraySum' function below.
--
-- The function is expected to return an INTEGER.
-- The function accepts INTEGER_ARRAY ar as parameter.
--

simpleArraySum = Data.List.foldr (+) 0

lstrip = Data.Text.unpack . Data.Text.stripStart . Data.Text.pack
rstrip = Data.Text.unpack . Data.Text.stripEnd . Data.Text.pack

main :: IO()
main = do
    stdout <- getEnv "OUTPUT_PATH"
    fptr <- openFile stdout WriteMode

    arCountTemp <- getLine
    let arCount = read $ lstrip $ rstrip arCountTemp :: Int

    arTemp <- getLine

    let ar = Data.List.map (read :: String -> Int) . Data.List.words $ rstrip arTemp

    let result = simpleArraySum ar

    hPutStrLn fptr $ show result

    hFlush fptr
    hClose fptr
