# Get stock prices using Julia
# http://dm13450.github.io/2020/07/05/AlphaVantage.html
using AlphaVantage
using DataFrames
using DataFramesMeta
using Dates
using Plots

#--- Settings
api_key = "XY5W322SZI5SHPCU"
AlphaVantage.global_key!(api_key)
AlphaVantage.GLOBAL[]

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
tslaRaw = AlphaVantage.time_series_daily_adjusted("TSLA", outputsize="full", datatype="csv")
tsla = raw_to_dataframe(tslaRaw);
first(tsla, 5)

plot(tsla.Date, tsla.open, label = "Open", title = "TSLA Daily")

#--- Intraday
# What separates AlphaVantage from say google or yahoo finance data is the intraday data. They provide high frequency bars at intervals from 1 minute to an hour. The only disadvantage is that the maximum amount of data appears to be 5 days for a stock. Still better than nothing!
tslaIntraRaw = AlphaVantage.time_series_intraday("TSLA", "1min", outputsize="full", datatype="csv");
tslaIntra = intra_to_dataframe(tslaIntraRaw)
tslaIntraDay = @where(tslaIntra, :DateTime .> DateTime(today()-Day(1)))
subPlot = plot(tslaIntraDay.DateTime, tslaIntraDay.open, label="Open", title="TSLA Intraday $(today()-Day(1))")
allPlot = plot(tslaIntra.DateTime, tslaIntra.open, label="Open", title = "TSLA Intraday")
plot(allPlot, subPlot, layout=(1,2))
