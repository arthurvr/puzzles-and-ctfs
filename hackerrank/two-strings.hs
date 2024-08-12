{-# LANGUAGE DuplicateRecordFields, FlexibleInstances, UndecidableInstances #-}

module Main where

import Control.Monad
import Data.Array
import Data.Bits
import Data.Set
import Debug.Trace
import Data.Text (pack, unpack, stripStart, stripEnd)
import System.Environment
import System.IO
import System.IO.Unsafe

--
-- Complete the 'twoStrings' function below.
--
-- The function is expected to return a STRING.
-- The function accepts following parameters:
--  1. STRING s1
--  2. STRING s2
--

format True = "YES"
format False = "NO"

twoStrings s1 s2 = format . not . Data.Set.null $ intersection (fromList s1) (fromList s2)

lstrip = unpack . stripStart . pack
rstrip = unpack . stripEnd . pack

main :: IO()
main = do
    stdout <- getEnv "OUTPUT_PATH"
    fptr <- openFile stdout WriteMode

    qTemp <- getLine
    let q = read $ lstrip $ rstrip qTemp :: Int

    forM_ [1..q] $ \q_itr -> do
        s1 <- getLine

        s2 <- getLine

        let result = twoStrings s1 s2

        hPutStrLn fptr result

    hFlush fptr
    hClose fptr
