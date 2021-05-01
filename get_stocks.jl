# Get stock prices using Julia
# http://dm13450.github.io/2020/07/05/AlphaVantage.html

using Pkg
Pkg.add("DataFramesMeta")

using AlphaVantage
using DataFrames
using DataFramesMeta
using Dates
using Plots

#--- Helper Functions
# convert between the raw data and Julia dataframes
function raw_to_dataframe(rawData)
    df = DataFrame(rawData[1])
    dfNames = Symbol.(vcat(rawData[2]...))
    df = rename(df, dfNames)

    df.Date = Date.(df.timestamp)
    for x in (:open, :high, :low, :close, :adjusted_close, :dividend_amount)
        df[!, x] = Float64.(df[!, x])
    end
    df.volume = Int64.(df.volume)
    return df
end

function intra_to_dataframe(rawData)
    df = DataFrame(rawData[1])
    dfNames = Symbol.(vcat(rawData[2]...))
    df = rename(df, dfNames)

    df.DateTime = DateTime.(df.timestamp, "yyyy-mm-dd HH:MM:SS")
    for x in (:open, :high, :low, :close)
        df[!, x] = Float64.(df[!, x])
    end
    df.volume = Int64.(df.volume)
    return df
end

#--- Stocks
# AlphaVantage provides daily, weekly and monthly historical stock data from 2000 right up to when you call the function. With the adjusted functions you also get dividends and adjusted closing prices to account for these dividends.
