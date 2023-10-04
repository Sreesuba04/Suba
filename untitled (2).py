# Sample data for water quality parameters (replace with actual data)
ph = 7.5
do = 6.0  # Dissolved Oxygen (mg/L)
bod = 3.0  # Biological Oxygen Demand (mg/L)
tc = 200.0  # Total Coliforms (MPN/100 mL)
fc = 10.0  # Fecal Coliforms (MPN/100 mL)

# Weight factors for each parameter (adjust as needed)
w_ph = 0.15
w_do = 0.10
w_bod = 0.20
w_tc = 0.25
w_fc = 0.30

# Function to calculate Water Quality Index (WQI)
def calculate_wqi(ph, do, bod, tc, fc):
    # Normalize the values
    ph_norm = (ph - 6.5) / (9.0 - 6.5)
    do_norm = (do - 0) / (14.0 - 0)
    bod_norm = (bod - 0) / (30.0 - 0)
    tc_norm = (tc - 0) / (5000 - 0)
    fc_norm = (fc - 0) / (5000 - 0)

    # Calculate sub-indices
    subindex_ph = 100 - 5 * ph_norm
    subindex_do = 100 - 5 * do_norm
    subindex_bod = 100 - 5 * bod_norm
    subindex_tc = 100 - 5 * tc_norm
    subindex_fc = 100 - 5 * fc_norm

    # Calculate WQI
    wqi = (w_ph * subindex_ph + w_do * subindex_do +
           w_bod * subindex_bod + w_tc * subindex_tc + w_fc * subindex_fc)

    return wqi

# Calculate and print the Water Quality Index
wqi_value = calculate_wqi(ph, do, bod, tc, fc)
print(f"Water Quality Index (WQI): {wqi_value:.2f}")
