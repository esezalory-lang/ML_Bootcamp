# Put this at the top of your kata04.py file

kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    sci_arg1 = "{:.2e}".format(kata[3])
    sci_arg2 = "{:.2e}".format(kata[4])
    print(f"module_{str(kata[0]).zfill(2)},",
          f"ex_{str(kata[1]).zfill(2)} :",
          f"{str(round(kata[2], 2))},",
          f"{sci_arg1}, {sci_arg2}")
