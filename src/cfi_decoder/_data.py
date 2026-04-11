"""ISO 10962 CFI code lookup tables.

Data sourced from the Wikipedia "Tabulated Structure of CFI Code" tables.
Each attribute is a (label, values_dict) tuple for self-documentation.
"""

AttrDef = tuple[str, dict[str, str]]

# ---------------------------------------------------------------------------
# Position 1: Category
# ---------------------------------------------------------------------------
CATEGORIES: dict[str, str] = {
    "E": "Equities",
    "D": "Debt Instruments",
    "C": "Collective Investment Vehicles",
    "O": "Listed Options",
    "F": "Futures",
    "H": "Non-Listed and Complex Listed Options",
    "I": "Spots",
    "J": "Forwards",
    "K": "Strategies",
    "L": "Financing",
    "T": "Referential Instruments",
    "M": "Others (Miscellaneous)",
}

# ---------------------------------------------------------------------------
# Position 2: Group (per category)
# ---------------------------------------------------------------------------
GROUPS: dict[str, dict[str, str]] = {
    "E": {
        "S": "Shares (Common/Ordinary)",
        "P": "Preferred Shares",
        "C": "Convertible Shares",
        "F": "Preferred Convertible Shares",
        "L": "Limited Partnership Units",
        "D": "Depository Receipts on Equities",
        "Y": "Structured Instruments (Participation)",
        "R": "Preference Shares",
        "V": "Preference Convertible Shares",
        "U": "Units (Unit Trusts/Mutual Funds)",
        "M": "Others (Miscellaneous)",
    },
    "D": {
        "B": "Bonds",
        "C": "Convertible Bonds",
        "W": "Bonds with Warrants Attached",
        "T": "Medium-Term Notes",
        "S": "Structured Products (Capital Protection)",
        "E": "Structured Products (No Capital Protection)",
        "G": "Mortgage-Backed Securities",
        "A": "Asset-Backed Securities",
        "N": "Municipal Bonds",
        "D": "Depository Receipts on Debt Instruments",
        "Y": "Money Market Instruments",
        "M": "Others (Miscellaneous)",
    },
    "C": {
        "I": "Standard Investment Funds/Mutual Funds",
        "H": "Hedge Funds",
        "B": "Real Estate Investment Trusts (REITs)",
        "E": "Exchange-Traded Funds (ETFs)",
        "S": "Pension Funds",
        "F": "Funds of Funds",
        "P": "Private Equity Funds",
        "R": "Entitlements (Rights)",
        "M": "Others (Miscellaneous)",
    },
    "O": {
        "C": "Call Options",
        "P": "Put Options",
        "M": "Others (Miscellaneous)",
    },
    "F": {
        "F": "Financial Futures",
        "C": "Commodities Futures",
    },
    "H": {
        "R": "Rates",
        "T": "Commodities",
        "E": "Equity",
        "C": "Credit",
        "F": "Foreign Exchange",
        "M": "Others (Miscellaneous)",
    },
    "I": {
        "F": "Foreign Exchange",
        "T": "Commodities",
    },
    "J": {
        "E": "Equity",
        "F": "Foreign Exchange",
        "C": "Credit",
        "R": "Rates",
        "T": "Commodities",
    },
    "K": {
        "R": "Rates",
        "T": "Commodities",
        "E": "Equity",
        "C": "Credit",
        "F": "Foreign Exchange",
        "Y": "Mixed Assets",
        "M": "Others (Miscellaneous)",
    },
    "L": {
        "L": "Loan Lease",
        "R": "Repurchase Agreements",
        "S": "Securities Lending",
    },
    "T": {
        "C": "Currencies",
        "T": "Commodities",
        "R": "Interest Rates",
        "I": "Indices",
        "B": "Baskets",
        "D": "Stock Dividends",
        "M": "Others (Miscellaneous)",
    },
    "M": {
        "C": "Combined Instruments",
        "M": "Others (Miscellaneous)",
    },
}

# ---------------------------------------------------------------------------
# Shared attribute definitions (reused across multiple groups)
# ---------------------------------------------------------------------------

_VOTING_RIGHT: AttrDef = (
    "Voting Right",
    {
        "V": "Voting",
        "N": "Non-Voting",
        "R": "Restricted Voting",
        "E": "Enhanced Voting",
    },
)

_OWNERSHIP: AttrDef = (
    "Ownership/Transfer",
    {"T": "Restrictions", "U": "Free"},
)

_PAYMENT_STATUS: AttrDef = (
    "Payment Status",
    {"F": "Fully Paid", "O": "Nil Paid", "P": "Partly Paid"},
)

_FORM: AttrDef = (
    "Form",
    {"B": "Bearer", "R": "Registered", "N": "Bearer/Registered", "M": "Others"},
)

_PREFERRED_REDEMPTION: AttrDef = (
    "Redemption/Conversion",
    {
        "R": "Redeemable",
        "E": "Extendible",
        "T": "Redeemable/Extendible",
        "G": "Exchangeable",
        "A": "Redeemable/Exchangeable/Extendible",
        "C": "Redeemable/Exchangeable",
        "N": "Perpetual",
    },
)

_PREFERRED_INCOME: AttrDef = (
    "Income",
    {
        "F": "Fixed Rate",
        "C": "Cumulative Fixed Rate",
        "P": "Participating",
        "Q": "Cumulative Participating",
        "A": "Adjustable/Variable Rate",
        "N": "Normal Rate",
        "U": "Auction Rate",
        "D": "Dividends",
    },
)

_DEBT_INTEREST: AttrDef = (
    "Type of Interest",
    {
        "F": "Fixed Rate",
        "Z": "Zero Rate/Discounted",
        "V": "Variable",
        "C": "Cash Payment",
        "K": "Payment in Kind",
    },
)

_DEBT_INTEREST_NO_K: AttrDef = (
    "Type of Interest",
    {
        "F": "Fixed Rate",
        "Z": "Zero Rate/Discounted",
        "V": "Variable",
    },
)

_DEBT_GUARANTEE: AttrDef = (
    "Guarantee",
    {
        "T": "Government/State Guarantee",
        "G": "Joint Guarantee",
        "S": "Secured",
        "U": "Unsecured/Unguaranteed",
        "P": "Negative Pledge",
        "N": "Senior",
        "O": "Senior Subordinated",
        "Q": "Junior",
        "J": "Junior Subordinated",
        "C": "Supranational",
    },
)

_DEBT_REDEMPTION: AttrDef = (
    "Redemption/Reimbursement",
    {
        "F": "Fixed Maturity",
        "G": "Fixed Maturity with Call Feature",
        "C": "Fixed Maturity with Put Feature",
        "D": "Fixed Maturity with Put and Call",
        "A": "Amortization Plan",
        "B": "Amortization Plan with Call Feature",
        "T": "Amortization Plan with Put Feature",
        "L": "Amortization Plan with Put and Call",
        "P": "Perpetual",
        "Q": "Perpetual with Call Feature",
        "R": "Perpetual with Put Feature",
        "E": "Extendible",
    },
)

_NOT_APPLICABLE: AttrDef = (
    "Not Applicable",
    {"X": "Not Applicable/Undefined"},
)

_ALL_X_ATTRS = (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE)

_CIV_SECURITY_TYPE: AttrDef = (
    "Security Type/Investor Restrictions",
    {
        "S": "Shares",
        "Q": "Shares for Qualified Investors",
        "U": "Units",
        "Y": "Units for Qualified Investors",
    },
)

_OPTION_EXERCISE: AttrDef = (
    "Exercise Option Style",
    {"A": "American", "E": "European", "B": "Bermudan"},
)

_OPTION_UNDERLYING: AttrDef = (
    "Underlying Asset",
    {
        "B": "Baskets",
        "S": "Stock-Equities",
        "D": "Debt Instruments",
        "T": "Commodities",
        "C": "Currencies",
        "I": "Indices",
        "O": "Options",
        "F": "Futures",
        "W": "Swaps",
        "N": "Interest Rates",
        "M": "Others",
    },
)

_OPTION_DELIVERY: AttrDef = (
    "Delivery",
    {
        "P": "Physical",
        "C": "Cash",
        "N": "Non-Deliverable",
        "E": "Elect at Exercise",
    },
)

_OPTION_STANDARD: AttrDef = (
    "Standardized/Non-Standardized",
    {"S": "Standardized", "N": "Non-Standardized"},
)

# ---------------------------------------------------------------------------
# Positions 3-6: Attributes (keyed by (category, group))
# ---------------------------------------------------------------------------
ATTRIBUTES: dict[tuple[str, str], tuple[AttrDef, AttrDef, AttrDef, AttrDef]] = {
    # -----------------------------------------------------------------------
    # E - Equities
    # -----------------------------------------------------------------------
    ("E", "S"): (_VOTING_RIGHT, _OWNERSHIP, _PAYMENT_STATUS, _FORM),
    ("E", "P"): (_VOTING_RIGHT, _PREFERRED_REDEMPTION, _PREFERRED_INCOME, _FORM),
    ("E", "C"): (_VOTING_RIGHT, _OWNERSHIP, _PAYMENT_STATUS, _FORM),
    ("E", "F"): (_VOTING_RIGHT, _PREFERRED_REDEMPTION, _PREFERRED_INCOME, _FORM),
    ("E", "L"): (_VOTING_RIGHT, _OWNERSHIP, _PAYMENT_STATUS, _FORM),
    ("E", "D"): (
        (
            "Instrument Dependency",
            {
                "S": "Common/Ordinary Shares",
                "P": "Preferred Shares",
                "C": "Common Convertible Shares",
                "F": "Preferred Convertible Shares",
                "L": "Limited Partnership Units",
                "M": "Others",
            },
        ),
        (
            "Redemption/Conversion",
            {
                "R": "Redeemable",
                "N": "Perpetual",
                "B": "Convertible",
                "D": "Convertible/Redeemable",
                "X": "Not Applicable/Undefined",
            },
        ),
        _PREFERRED_INCOME,
        _FORM,
    ),
    ("E", "Y"): (
        (
            "Type",
            {
                "A": "Tracker Certificate",
                "B": "Outperforming Certificate",
                "C": "Bonus Certificate",
                "D": "Outperformance Bonus Certificate",
                "E": "Twin-Win Certificate",
                "M": "Others",
            },
        ),
        (
            "Distribution",
            {"D": "Dividend Payments", "Y": "No Payments", "M": "Others"},
        ),
        (
            "Repayment",
            {
                "F": "Cash Repayment",
                "V": "Physical Repayment",
                "E": "Elect at Settlement",
                "M": "Others",
            },
        ),
        (
            "Underlying Asset",
            {
                "B": "Baskets",
                "S": "Equities",
                "D": "Debt Instruments",
                "G": "Derivatives",
                "T": "Commodities",
                "C": "Currencies",
                "I": "Indices",
                "N": "Interest Rates",
                "M": "Others",
            },
        ),
    ),
    ("E", "R"): (_VOTING_RIGHT, _PREFERRED_REDEMPTION, _PREFERRED_INCOME, _FORM),
    ("E", "V"): (_VOTING_RIGHT, _PREFERRED_REDEMPTION, _PREFERRED_INCOME, _FORM),
    ("E", "U"): (
        (
            "Closed/Open-End",
            {"C": "Closed-End", "O": "Open-End"},
        ),
        (
            "Distribution Policy",
            {"I": "Income Funds", "G": "Growth Funds", "M": "Mixed Funds"},
        ),
        (
            "Assets",
            {
                "R": "Real Estate",
                "S": "Securities",
                "M": "Mixed-General",
                "C": "Commodities",
                "D": "Derivatives",
            },
        ),
        (
            "Form",
            {
                "B": "Bearer",
                "R": "Registered",
                "N": "Bearer/Registered",
                "Z": "Bearer Depository Receipt",
                "A": "Registered Depository Receipt",
                "M": "Others",
            },
        ),
    ),
    ("E", "M"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _FORM),
    # -----------------------------------------------------------------------
    # D - Debt Instruments
    # -----------------------------------------------------------------------
    ("D", "B"): (_DEBT_INTEREST, _DEBT_GUARANTEE, _DEBT_REDEMPTION, _FORM),
    ("D", "C"): (_DEBT_INTEREST, _DEBT_GUARANTEE, _DEBT_REDEMPTION, _FORM),
    ("D", "W"): (_DEBT_INTEREST, _DEBT_GUARANTEE, _DEBT_REDEMPTION, _FORM),
    ("D", "T"): (_DEBT_INTEREST, _DEBT_GUARANTEE, _DEBT_REDEMPTION, _FORM),
    ("D", "S"): (
        (
            "Type",
            {
                "A": "Capital Protection Certificate with Participation",
                "B": "Capital Protection Convertible Certificate",
                "C": "Barrier Capital Protection Certificate",
                "D": "Capital Protection Certificate with Coupons",
                "M": "Others",
            },
        ),
        (
            "Distribution",
            {
                "F": "Fixed Interest Payments",
                "D": "Dividend Payments",
                "V": "Variable Interest Payments",
                "Y": "No Payments",
                "M": "Others",
            },
        ),
        (
            "Repayment",
            {
                "F": "Fixed Cash Repayment (Protected Capital Level)",
                "V": "Variable Cash Repayment",
                "M": "Others",
            },
        ),
        (
            "Underlying Asset",
            {
                "B": "Baskets",
                "S": "Equities",
                "D": "Debt Instruments/Interest Rates",
                "T": "Commodities",
                "C": "Currencies",
                "I": "Indices",
                "M": "Others",
            },
        ),
    ),
    ("D", "E"): (
        (
            "Type",
            {
                "A": "Discount Certificate",
                "B": "Barrier Discount Certificate",
                "C": "Reverse Convertible",
                "D": "Barrier Reverse Convertible",
                "E": "Express Certificate",
                "M": "Others",
            },
        ),
        (
            "Repayment",
            {
                "R": "Repayment in Cash",
                "S": "Repayment in Assets",
                "C": "Repayment in Assets and Cash",
                "T": "Repayment in Assets or Cash",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
    ("D", "G"): (_DEBT_INTEREST_NO_K, _DEBT_GUARANTEE, _DEBT_REDEMPTION, _FORM),
    ("D", "A"): (_DEBT_INTEREST_NO_K, _DEBT_GUARANTEE, _DEBT_REDEMPTION, _FORM),
    ("D", "N"): (_DEBT_INTEREST_NO_K, _DEBT_GUARANTEE, _DEBT_REDEMPTION, _FORM),
    ("D", "D"): (
        (
            "Instrument Dependency",
            {
                "B": "Bonds",
                "C": "Convertible Bonds",
                "W": "Bonds with Warrants",
                "T": "Medium-Term Notes",
                "Y": "Money Market Instruments",
                "G": "Mortgage-Backed Securities",
                "Q": "Asset-Backed Securities",
                "N": "Municipal Bonds",
                "M": "Others",
            },
        ),
        (
            "Type of Interest/Cash Payment",
            {
                "F": "Fixed Rate",
                "Z": "Zero Rate/Discounted",
                "V": "Variable",
                "C": "Cash Payment",
            },
        ),
        _DEBT_GUARANTEE,
        _DEBT_REDEMPTION,
    ),
    ("D", "Y"): (
        (
            "Type of Interest",
            {
                "F": "Fixed Rate",
                "Z": "Zero Rate/Discounted",
                "V": "Variable",
                "K": "Payment in Kind",
            },
        ),
        _DEBT_GUARANTEE,
        _NOT_APPLICABLE,
        _FORM,
    ),
    ("D", "M"): (
        (
            "Type",
            {"B": "Bank Loan", "P": "Promissory Note", "M": "Others"},
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _FORM,
    ),
    # -----------------------------------------------------------------------
    # C - Collective Investment Vehicles
    # -----------------------------------------------------------------------
    ("C", "I"): (
        (
            "Closed/Open-End",
            {"O": "Open-End", "C": "Closed-End", "M": "Others"},
        ),
        (
            "Distribution Policy",
            {"I": "Income Funds", "G": "Accumulation Funds", "J": "Mixed Funds"},
        ),
        (
            "Assets",
            {
                "R": "Real Estate",
                "B": "Debt Instruments",
                "E": "Equities",
                "V": "Convertible Securities",
                "L": "Mixed",
                "C": "Commodities",
                "D": "Derivatives",
                "F": "Referential Instruments",
                "K": "Credits",
                "M": "Others",
            },
        ),
        _CIV_SECURITY_TYPE,
    ),
    ("C", "H"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _CIV_SECURITY_TYPE),
    ("C", "B"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _CIV_SECURITY_TYPE),
    ("C", "E"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _CIV_SECURITY_TYPE),
    ("C", "S"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _CIV_SECURITY_TYPE),
    ("C", "F"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _CIV_SECURITY_TYPE),
    ("C", "P"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _CIV_SECURITY_TYPE),
    ("C", "M"): (_NOT_APPLICABLE, _NOT_APPLICABLE, _NOT_APPLICABLE, _CIV_SECURITY_TYPE),
    ("C", "R"): (
        (
            "Entitlement Type",
            {
                "A": "Allotment (Bonus) Rights",
                "S": "Subscription Rights",
                "P": "Purchase Rights",
                "W": "Warrants",
                "F": "Mini-Future Certificates/Constant Leverage Certificates",
                "D": "Depository Receipts on Entitlements",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _FORM,
    ),
    # -----------------------------------------------------------------------
    # O - Listed Options
    # -----------------------------------------------------------------------
    ("O", "C"): (
        _OPTION_EXERCISE,
        _OPTION_UNDERLYING,
        _OPTION_DELIVERY,
        _OPTION_STANDARD,
    ),
    ("O", "P"): (
        _OPTION_EXERCISE,
        _OPTION_UNDERLYING,
        _OPTION_DELIVERY,
        _OPTION_STANDARD,
    ),
    ("O", "M"): _ALL_X_ATTRS,
    # -----------------------------------------------------------------------
    # F - Futures
    # -----------------------------------------------------------------------
    ("F", "F"): (
        (
            "Underlying Asset",
            {
                "B": "Baskets",
                "S": "Stock-Equities",
                "D": "Debt Instruments",
                "C": "Currencies",
                "I": "Indices",
                "O": "Options",
                "F": "Futures",
                "W": "Swaps",
                "N": "Interest Rates",
                "V": "Stock Dividend",
                "M": "Others",
            },
        ),
        (
            "Delivery",
            {"P": "Physical", "C": "Cash", "N": "Non-Deliverable"},
        ),
        _OPTION_STANDARD,
        _NOT_APPLICABLE,
    ),
    ("F", "C"): (
        (
            "Underlying Asset",
            {
                "E": "Extraction Resources",
                "A": "Agriculture",
                "I": "Industrial Products",
                "S": "Services",
                "N": "Environmental",
                "P": "Polypropylene Products",
                "H": "Generated Resources",
                "M": "Others",
            },
        ),
        (
            "Delivery",
            {"P": "Physical", "C": "Cash", "N": "Non-Deliverable"},
        ),
        _OPTION_STANDARD,
        _NOT_APPLICABLE,
    ),
    # -----------------------------------------------------------------------
    # H - Non-Listed and Complex Listed Options (all X)
    # -----------------------------------------------------------------------
    ("H", "R"): _ALL_X_ATTRS,
    ("H", "T"): _ALL_X_ATTRS,
    ("H", "E"): _ALL_X_ATTRS,
    ("H", "C"): _ALL_X_ATTRS,
    ("H", "F"): _ALL_X_ATTRS,
    ("H", "M"): _ALL_X_ATTRS,
    # -----------------------------------------------------------------------
    # I - Spots
    # -----------------------------------------------------------------------
    ("I", "F"): (
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        ("Delivery", {"P": "Physical"}),
    ),
    ("I", "T"): (
        (
            "Underlying Asset",
            {
                "A": "Agriculture",
                "J": "Energy",
                "K": "Metals",
                "N": "Environmental",
                "P": "Polypropylene Products",
                "S": "Fertilizer",
                "T": "Paper",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
    # -----------------------------------------------------------------------
    # J - Forwards (all X)
    # -----------------------------------------------------------------------
    ("J", "E"): _ALL_X_ATTRS,
    ("J", "F"): _ALL_X_ATTRS,
    ("J", "C"): _ALL_X_ATTRS,
    ("J", "R"): _ALL_X_ATTRS,
    ("J", "T"): _ALL_X_ATTRS,
    # -----------------------------------------------------------------------
    # K - Strategies (all X)
    # -----------------------------------------------------------------------
    ("K", "R"): _ALL_X_ATTRS,
    ("K", "T"): _ALL_X_ATTRS,
    ("K", "E"): _ALL_X_ATTRS,
    ("K", "C"): _ALL_X_ATTRS,
    ("K", "F"): _ALL_X_ATTRS,
    ("K", "Y"): _ALL_X_ATTRS,
    ("K", "M"): _ALL_X_ATTRS,
    # -----------------------------------------------------------------------
    # L - Financing
    # -----------------------------------------------------------------------
    ("L", "L"): (
        (
            "Underlying Asset",
            {
                "A": "Agriculture",
                "B": "Baskets",
                "J": "Energy",
                "K": "Metals",
                "N": "Environmental",
                "P": "Polypropylene Products",
                "S": "Fertilizer",
                "T": "Paper",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        (
            "Delivery",
            {"P": "Physical", "C": "Cash", "N": "Non-Deliverable"},
        ),
    ),
    ("L", "R"): (
        (
            "Underlying Asset",
            {
                "G": "General Collateral",
                "S": "Specific Security Collateral",
                "C": "Cash Collateral",
            },
        ),
        (
            "Termination",
            {
                "F": "Flexible",
                "N": "Overnight",
                "O": "Open",
                "T": "Term",
            },
        ),
        _NOT_APPLICABLE,
        (
            "Delivery",
            {
                "D": "Delivery versus Payment",
                "H": "Hold-in-Custody",
                "T": "Tri-Party",
            },
        ),
    ),
    ("L", "S"): (
        (
            "Underlying Asset",
            {
                "C": "Cash Collateral",
                "G": "Government Bonds",
                "P": "Corporate Bonds",
                "T": "Convertible Bonds",
                "E": "Equity",
                "L": "Letter of Credit",
                "D": "Certificate of Deposit",
                "W": "Warrants",
                "K": "Money Market Instruments",
                "M": "Others",
            },
        ),
        (
            "Termination",
            {"N": "Overnight", "O": "Open", "T": "Term"},
        ),
        _NOT_APPLICABLE,
        (
            "Delivery",
            {
                "D": "Delivery versus Payment",
                "F": "Free of Payment",
                "H": "Hold-in-Custody",
                "T": "Tri-Party",
            },
        ),
    ),
    # -----------------------------------------------------------------------
    # T - Referential Instruments
    # -----------------------------------------------------------------------
    ("T", "C"): (
        (
            "Type",
            {
                "N": "National Currency",
                "L": "Legacy Currency",
                "C": "Bullion Coins",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
    ("T", "T"): (
        (
            "Underlying Asset",
            {
                "E": "Extraction Resources",
                "A": "Agriculture",
                "I": "Industrial Products",
                "S": "Services",
                "N": "Environmental",
                "P": "Polypropylene Products",
                "H": "Generated Resources",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
    ("T", "R"): (
        (
            "Type",
            {
                "N": "Nominal",
                "V": "Variable",
                "F": "Fixed",
                "R": "Real",
                "M": "Others",
            },
        ),
        (
            "Frequency of Calculation",
            {
                "D": "Daily",
                "W": "Weekly",
                "N": "Monthly",
                "Q": "Quarterly",
                "S": "Semi-Annually",
                "A": "Annually",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
    ("T", "I"): (
        (
            "Asset Class",
            {
                "E": "Equities",
                "D": "Debt",
                "F": "Collective Investment Vehicles",
                "R": "Real Estate",
                "T": "Commodities",
                "C": "Currencies",
                "M": "Others",
            },
        ),
        (
            "Weighting Type",
            {
                "P": "Price Weighted",
                "C": "Capitalization Weighted",
                "E": "Equal Weighted",
                "F": "Modified Market Capitalization Weighted",
                "M": "Others",
            },
        ),
        (
            "Index Return Type",
            {
                "P": "Price Return",
                "N": "Net Total Return",
                "G": "Gross Total Return",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
    ),
    ("T", "B"): (
        (
            "Composition",
            {
                "E": "Equities",
                "D": "Debt",
                "F": "Collective Investment Vehicles",
                "I": "Indices",
                "T": "Commodities",
                "C": "Currencies",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
    ("T", "D"): (
        (
            "Type of Equity",
            {
                "S": "Common/Ordinary Shares",
                "P": "Preferred/Preference Shares",
                "C": "Common/Ordinary Convertible Shares",
                "F": "Preferred/Preference Convertible Shares",
                "L": "Limited Partnership Units",
                "K": "Collective Investment Vehicles",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
    ("T", "M"): _ALL_X_ATTRS,
    # -----------------------------------------------------------------------
    # M - Miscellaneous/Others
    # -----------------------------------------------------------------------
    ("M", "C"): (
        (
            "Component",
            {
                "S": "Combination of Shares",
                "B": "Combination of Bonds",
                "H": "Share and Bond",
                "A": "Share and Warrant",
                "W": "Warrant and Warrant",
                "U": "Fund Units and Other Components",
                "M": "Others",
            },
        ),
        _OWNERSHIP,
        _NOT_APPLICABLE,
        _FORM,
    ),
    ("M", "M"): (
        (
            "Further Grouping",
            {
                "R": "Real Estate Deeds",
                "I": "Insurance Policies",
                "E": "Escrow Receipts",
                "T": "Trade Finance Instruments",
                "N": "Carbon Credit",
                "P": "Precious Metal Receipts",
                "S": "Other OTC Derivative Products",
                "M": "Others",
            },
        ),
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
        _NOT_APPLICABLE,
    ),
}
