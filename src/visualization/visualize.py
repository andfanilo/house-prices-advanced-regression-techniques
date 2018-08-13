import pandas_profiling


def create_pandas_profiling(df, output_path):
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(outputfile=output_path)


