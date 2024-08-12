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
-- Complete the 'angryProfessor' function below.
--
-- The function is expected to return a STRING.
-- The function accepts following parameters:
--  1. INTEGER k
--  2. INTEGER_ARRAY a
--

angryProfessor k a = format $ ((Data.List.length a) - (late a)) < k
    where late = Data.List.length . Data.List.filter (> 0)
          format True = "YES"
          format False = "NO"

lstrip = Data.Text.unpack . Data.Text.stripStart . Data.Text.pack
rstrip = Data.Text.unpack . Data.Text.stripEnd . Data.Text.pack

main :: IO()
main = do
    stdout <- getEnv "OUTPUT_PATH"
    fptr <- openFile stdout WriteMode

    tTemp <- getLine
    let t = read $ lstrip $ rstrip tTemp :: Int

    forM_ [1..t] $ \t_itr -> do
        firstMultipleInputTemp <- getLine
        let firstMultipleInput = Data.List.words $ rstrip firstMultipleInputTemp

        let n = read (firstMultipleInput !! 0) :: Int

        let k = read (firstMultipleInput !! 1) :: Int

        aTemp <- getLine

        let a = Data.List.map (read :: String -> Int) . Data.List.words $ rstrip aTemp

        let result = angryProfessor k a

        hPutStrLn fptr result

    hFlush fptr
    hClose fptr
