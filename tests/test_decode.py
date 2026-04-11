"""Tests for the cfi_decoder.decode function."""

import pytest

from cfi_decoder import decode

# ---------------------------------------------------------------------------
# E - Equities
# ---------------------------------------------------------------------------


class TestEquitiesShares:
    def test_voting_free_fully_paid_registered(self) -> None:
        assert decode("ESVUFR") == (
            "Equities | Shares (Common/Ordinary)"
            " | Voting | Free | Fully Paid | Registered"
        )

    def test_non_voting_restrictions_nil_paid_bearer(self) -> None:
        assert decode("ESNTOB") == (
            "Equities | Shares (Common/Ordinary)"
            " | Non-Voting | Restrictions | Nil Paid | Bearer"
        )

    def test_restricted_voting_partly_paid_bearer_registered(self) -> None:
        assert decode("ESRUPN") == (
            "Equities | Shares (Common/Ordinary)"
            " | Restricted Voting | Free | Partly Paid | Bearer/Registered"
        )

    def test_enhanced_voting_others_form(self) -> None:
        assert decode("ESETFM") == (
            "Equities | Shares (Common/Ordinary)"
            " | Enhanced Voting | Restrictions | Fully Paid | Others"
        )


class TestEquitiesPreferred:
    def test_voting_redeemable_fixed_rate_bearer(self) -> None:
        assert decode("EPVRFB") == (
            "Equities | Preferred Shares | Voting | Redeemable | Fixed Rate | Bearer"
        )

    def test_non_voting_extendible_cumulative_fixed(self) -> None:
        assert decode("EPNECR") == (
            "Equities | Preferred Shares"
            " | Non-Voting | Extendible | Cumulative Fixed Rate | Registered"
        )

    def test_perpetual_participating(self) -> None:
        assert decode("EPRNPB") == (
            "Equities | Preferred Shares"
            " | Restricted Voting | Perpetual | Participating | Bearer"
        )

    def test_exchangeable_cumulative_participating(self) -> None:
        assert decode("EPVGQN") == (
            "Equities | Preferred Shares"
            " | Voting | Exchangeable | Cumulative Participating"
            " | Bearer/Registered"
        )

    def test_redeemable_extendible_adjustable(self) -> None:
        assert decode("EPVTAN") == (
            "Equities | Preferred Shares"
            " | Voting | Redeemable/Extendible | Adjustable/Variable Rate"
            " | Bearer/Registered"
        )

    def test_redeemable_exchangeable_extendible_normal_rate(self) -> None:
        assert decode("EPVANR") == (
            "Equities | Preferred Shares"
            " | Voting | Redeemable/Exchangeable/Extendible"
            " | Normal Rate | Registered"
        )

    def test_redeemable_exchangeable_auction_rate(self) -> None:
        assert decode("EPVCUB") == (
            "Equities | Preferred Shares"
            " | Voting | Redeemable/Exchangeable | Auction Rate | Bearer"
        )

    def test_dividends_income(self) -> None:
        assert decode("EPVRDR") == (
            "Equities | Preferred Shares | Voting | Redeemable | Dividends | Registered"
        )


class TestEquitiesConvertible:
    def test_voting_free_fully_paid(self) -> None:
        assert decode("ECVUFR") == (
            "Equities | Convertible Shares | Voting | Free | Fully Paid | Registered"
        )

    def test_non_voting_restrictions_nil_paid(self) -> None:
        assert decode("ECNTOB") == (
            "Equities | Convertible Shares"
            " | Non-Voting | Restrictions | Nil Paid | Bearer"
        )


class TestEquitiesPreferredConvertible:
    def test_basic(self) -> None:
        assert decode("EFVRFB") == (
            "Equities | Preferred Convertible Shares"
            " | Voting | Redeemable | Fixed Rate | Bearer"
        )

    def test_perpetual_dividends(self) -> None:
        assert decode("EFNNDR") == (
            "Equities | Preferred Convertible Shares"
            " | Non-Voting | Perpetual | Dividends | Registered"
        )


class TestEquitiesLimitedPartnership:
    def test_basic(self) -> None:
        assert decode("ELVUFR") == (
            "Equities | Limited Partnership Units"
            " | Voting | Free | Fully Paid | Registered"
        )

    def test_restricted_partly_paid(self) -> None:
        assert decode("ELRTPN") == (
            "Equities | Limited Partnership Units"
            " | Restricted Voting | Restrictions | Partly Paid"
            " | Bearer/Registered"
        )


class TestEquitiesDepositoryReceipts:
    def test_common_shares_redeemable(self) -> None:
        assert decode("EDSRFR") == (
            "Equities | Depository Receipts on Equities"
            " | Common/Ordinary Shares | Redeemable | Fixed Rate | Registered"
        )

    def test_preferred_shares_perpetual(self) -> None:
        assert decode("EDPNCB") == (
            "Equities | Depository Receipts on Equities"
            " | Preferred Shares | Perpetual | Cumulative Fixed Rate | Bearer"
        )

    def test_convertible_shares_convertible(self) -> None:
        assert decode("EDCBPR") == (
            "Equities | Depository Receipts on Equities"
            " | Common Convertible Shares | Convertible | Participating"
            " | Registered"
        )

    def test_preferred_convertible_convertible_redeemable(self) -> None:
        assert decode("EDFDQN") == (
            "Equities | Depository Receipts on Equities"
            " | Preferred Convertible Shares | Convertible/Redeemable"
            " | Cumulative Participating | Bearer/Registered"
        )

    def test_limited_partnership_not_applicable(self) -> None:
        assert decode("EDLXAR") == (
            "Equities | Depository Receipts on Equities"
            " | Limited Partnership Units | Not Applicable/Undefined"
            " | Adjustable/Variable Rate | Registered"
        )

    def test_others_auction_rate(self) -> None:
        assert decode("EDMRUB") == (
            "Equities | Depository Receipts on Equities"
            " | Others | Redeemable | Auction Rate | Bearer"
        )


class TestEquitiesStructuredParticipation:
    def test_tracker_certificate(self) -> None:
        assert decode("EYADFS") == (
            "Equities | Structured Instruments (Participation)"
            " | Tracker Certificate | Dividend Payments"
            " | Cash Repayment | Equities"
        )

    def test_outperforming_no_payments_physical(self) -> None:
        assert decode("EYBYVI") == (
            "Equities | Structured Instruments (Participation)"
            " | Outperforming Certificate | No Payments"
            " | Physical Repayment | Indices"
        )

    def test_bonus_certificate_elect_settlement(self) -> None:
        assert decode("EYCMET") == (
            "Equities | Structured Instruments (Participation)"
            " | Bonus Certificate | Others | Elect at Settlement | Commodities"
        )

    def test_outperformance_bonus(self) -> None:
        assert decode("EYDDFC") == (
            "Equities | Structured Instruments (Participation)"
            " | Outperformance Bonus Certificate | Dividend Payments"
            " | Cash Repayment | Currencies"
        )

    def test_twin_win_baskets(self) -> None:
        assert decode("EYEYFB") == (
            "Equities | Structured Instruments (Participation)"
            " | Twin-Win Certificate | No Payments"
            " | Cash Repayment | Baskets"
        )

    def test_others_derivatives(self) -> None:
        assert decode("EYMDMG") == (
            "Equities | Structured Instruments (Participation)"
            " | Others | Dividend Payments | Others | Derivatives"
        )

    def test_underlying_debt_instruments(self) -> None:
        assert decode("EYADFD") == (
            "Equities | Structured Instruments (Participation)"
            " | Tracker Certificate | Dividend Payments"
            " | Cash Repayment | Debt Instruments"
        )

    def test_underlying_interest_rates(self) -> None:
        assert decode("EYADFN") == (
            "Equities | Structured Instruments (Participation)"
            " | Tracker Certificate | Dividend Payments"
            " | Cash Repayment | Interest Rates"
        )


class TestEquitiesPreferenceShares:
    def test_basic(self) -> None:
        assert decode("ERVRFB") == (
            "Equities | Preference Shares | Voting | Redeemable | Fixed Rate | Bearer"
        )

    def test_enhanced_perpetual_auction(self) -> None:
        assert decode("ERENUN") == (
            "Equities | Preference Shares"
            " | Enhanced Voting | Perpetual | Auction Rate"
            " | Bearer/Registered"
        )


class TestEquitiesPreferenceConvertible:
    def test_basic(self) -> None:
        assert decode("EVVRFB") == (
            "Equities | Preference Convertible Shares"
            " | Voting | Redeemable | Fixed Rate | Bearer"
        )

    def test_exchangeable_adjustable(self) -> None:
        assert decode("EVEGAR") == (
            "Equities | Preference Convertible Shares"
            " | Enhanced Voting | Exchangeable | Adjustable/Variable Rate"
            " | Registered"
        )


class TestEquitiesUnits:
    def test_open_end_income_real_estate(self) -> None:
        assert decode("EUOIRB") == (
            "Equities | Units (Unit Trusts/Mutual Funds)"
            " | Open-End | Income Funds | Real Estate | Bearer"
        )

    def test_closed_end_growth_securities(self) -> None:
        assert decode("EUCGSR") == (
            "Equities | Units (Unit Trusts/Mutual Funds)"
            " | Closed-End | Growth Funds | Securities | Registered"
        )

    def test_mixed_funds_commodities(self) -> None:
        assert decode("EUOMCN") == (
            "Equities | Units (Unit Trusts/Mutual Funds)"
            " | Open-End | Mixed Funds | Commodities | Bearer/Registered"
        )

    def test_derivatives_bearer_depository(self) -> None:
        assert decode("EUOIDZ") == (
            "Equities | Units (Unit Trusts/Mutual Funds)"
            " | Open-End | Income Funds | Derivatives | Bearer Depository Receipt"
        )

    def test_registered_depository(self) -> None:
        assert decode("EUOISA") == (
            "Equities | Units (Unit Trusts/Mutual Funds)"
            " | Open-End | Income Funds | Securities"
            " | Registered Depository Receipt"
        )

    def test_mixed_general_others_form(self) -> None:
        assert decode("EUOGMM") == (
            "Equities | Units (Unit Trusts/Mutual Funds)"
            " | Open-End | Growth Funds | Mixed-General | Others"
        )


class TestEquitiesMisc:
    def test_all_not_applicable_bearer(self) -> None:
        assert decode("EMXXXB") == (
            "Equities | Others (Miscellaneous)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Bearer"
        )

    def test_registered(self) -> None:
        assert decode("EMXXXR") == (
            "Equities | Others (Miscellaneous)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Registered"
        )


# ---------------------------------------------------------------------------
# D - Debt Instruments
# ---------------------------------------------------------------------------


class TestDebtBonds:
    def test_fixed_secured_fixed_maturity_bearer(self) -> None:
        assert decode("DBFSFB") == (
            "Debt Instruments | Bonds | Fixed Rate | Secured | Fixed Maturity | Bearer"
        )

    def test_zero_rate_government_guarantee(self) -> None:
        assert decode("DBZTGR") == (
            "Debt Instruments | Bonds"
            " | Zero Rate/Discounted | Government/State Guarantee"
            " | Fixed Maturity with Call Feature | Registered"
        )

    def test_variable_joint_guarantee_put(self) -> None:
        assert decode("DBVGCN") == (
            "Debt Instruments | Bonds"
            " | Variable | Joint Guarantee | Fixed Maturity with Put Feature"
            " | Bearer/Registered"
        )

    def test_cash_payment_negative_pledge(self) -> None:
        assert decode("DBCPDB") == (
            "Debt Instruments | Bonds"
            " | Cash Payment | Negative Pledge"
            " | Fixed Maturity with Put and Call | Bearer"
        )

    def test_payment_in_kind_senior(self) -> None:
        assert decode("DBKNAR") == (
            "Debt Instruments | Bonds"
            " | Payment in Kind | Senior | Amortization Plan | Registered"
        )

    def test_senior_subordinated_amortization_call(self) -> None:
        assert decode("DBFOBR") == (
            "Debt Instruments | Bonds"
            " | Fixed Rate | Senior Subordinated"
            " | Amortization Plan with Call Feature | Registered"
        )

    def test_junior_amortization_put(self) -> None:
        assert decode("DBFQTB") == (
            "Debt Instruments | Bonds"
            " | Fixed Rate | Junior | Amortization Plan with Put Feature | Bearer"
        )

    def test_junior_subordinated_amortization_put_and_call(self) -> None:
        assert decode("DBFJLN") == (
            "Debt Instruments | Bonds"
            " | Fixed Rate | Junior Subordinated"
            " | Amortization Plan with Put and Call | Bearer/Registered"
        )

    def test_supranational_perpetual(self) -> None:
        assert decode("DBFCPR") == (
            "Debt Instruments | Bonds"
            " | Fixed Rate | Supranational | Perpetual | Registered"
        )

    def test_perpetual_with_call(self) -> None:
        assert decode("DBFSQB") == (
            "Debt Instruments | Bonds"
            " | Fixed Rate | Secured | Perpetual with Call Feature | Bearer"
        )

    def test_perpetual_with_put(self) -> None:
        assert decode("DBFSRR") == (
            "Debt Instruments | Bonds"
            " | Fixed Rate | Secured | Perpetual with Put Feature | Registered"
        )

    def test_extendible(self) -> None:
        assert decode("DBFSEM") == (
            "Debt Instruments | Bonds | Fixed Rate | Secured | Extendible | Others"
        )

    def test_unsecured(self) -> None:
        assert decode("DBFUFB") == (
            "Debt Instruments | Bonds"
            " | Fixed Rate | Unsecured/Unguaranteed | Fixed Maturity | Bearer"
        )


class TestDebtConvertibleBonds:
    def test_variable_unsecured(self) -> None:
        assert decode("DCVUFR") == (
            "Debt Instruments | Convertible Bonds"
            " | Variable | Unsecured/Unguaranteed | Fixed Maturity | Registered"
        )

    def test_zero_rate_secured(self) -> None:
        assert decode("DCZSAB") == (
            "Debt Instruments | Convertible Bonds"
            " | Zero Rate/Discounted | Secured | Amortization Plan | Bearer"
        )


class TestDebtBondsWithWarrants:
    def test_fixed_secured(self) -> None:
        assert decode("DWFSFR") == (
            "Debt Instruments | Bonds with Warrants Attached"
            " | Fixed Rate | Secured | Fixed Maturity | Registered"
        )

    def test_variable_government(self) -> None:
        assert decode("DWVTGB") == (
            "Debt Instruments | Bonds with Warrants Attached"
            " | Variable | Government/State Guarantee"
            " | Fixed Maturity with Call Feature | Bearer"
        )


class TestDebtMediumTermNotes:
    def test_fixed_senior(self) -> None:
        assert decode("DTFNFR") == (
            "Debt Instruments | Medium-Term Notes"
            " | Fixed Rate | Senior | Fixed Maturity | Registered"
        )

    def test_cash_payment_perpetual(self) -> None:
        assert decode("DTCUPB") == (
            "Debt Instruments | Medium-Term Notes"
            " | Cash Payment | Unsecured/Unguaranteed | Perpetual | Bearer"
        )


class TestDebtStructuredCapitalProtection:
    def test_participation_fixed_interest(self) -> None:
        assert decode("DSAFFS") == (
            "Debt Instruments | Structured Products (Capital Protection)"
            " | Capital Protection Certificate with Participation"
            " | Fixed Interest Payments"
            " | Fixed Cash Repayment (Protected Capital Level)"
            " | Equities"
        )

    def test_convertible_certificate_dividends(self) -> None:
        assert decode("DSBDVB") == (
            "Debt Instruments | Structured Products (Capital Protection)"
            " | Capital Protection Convertible Certificate"
            " | Dividend Payments | Variable Cash Repayment | Baskets"
        )

    def test_barrier_variable_interest(self) -> None:
        assert decode("DSCVMI") == (
            "Debt Instruments | Structured Products (Capital Protection)"
            " | Barrier Capital Protection Certificate"
            " | Variable Interest Payments | Others | Indices"
        )

    def test_coupons_no_payments(self) -> None:
        assert decode("DSDYFT") == (
            "Debt Instruments | Structured Products (Capital Protection)"
            " | Capital Protection Certificate with Coupons"
            " | No Payments"
            " | Fixed Cash Repayment (Protected Capital Level)"
            " | Commodities"
        )

    def test_others_type_currencies(self) -> None:
        assert decode("DSMFFC") == (
            "Debt Instruments | Structured Products (Capital Protection)"
            " | Others | Fixed Interest Payments"
            " | Fixed Cash Repayment (Protected Capital Level)"
            " | Currencies"
        )

    def test_underlying_debt(self) -> None:
        assert decode("DSAFFD") == (
            "Debt Instruments | Structured Products (Capital Protection)"
            " | Capital Protection Certificate with Participation"
            " | Fixed Interest Payments"
            " | Fixed Cash Repayment (Protected Capital Level)"
            " | Debt Instruments/Interest Rates"
        )


class TestDebtStructuredNoCapitalProtection:
    def test_discount_certificate_cash(self) -> None:
        assert decode("DEARXX") == (
            "Debt Instruments | Structured Products (No Capital Protection)"
            " | Discount Certificate | Repayment in Cash"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_barrier_discount_assets(self) -> None:
        assert decode("DEBSXX") == (
            "Debt Instruments | Structured Products (No Capital Protection)"
            " | Barrier Discount Certificate | Repayment in Assets"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_reverse_convertible_assets_and_cash(self) -> None:
        assert decode("DECCXX") == (
            "Debt Instruments | Structured Products (No Capital Protection)"
            " | Reverse Convertible | Repayment in Assets and Cash"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_barrier_reverse_convertible_assets_or_cash(self) -> None:
        assert decode("DEDTXX") == (
            "Debt Instruments | Structured Products (No Capital Protection)"
            " | Barrier Reverse Convertible | Repayment in Assets or Cash"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_express_certificate(self) -> None:
        assert decode("DEEMXX") == (
            "Debt Instruments | Structured Products (No Capital Protection)"
            " | Express Certificate | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )


class TestDebtMBS:
    def test_fixed_secured(self) -> None:
        assert decode("DGFSFR") == (
            "Debt Instruments | Mortgage-Backed Securities"
            " | Fixed Rate | Secured | Fixed Maturity | Registered"
        )

    def test_zero_rate_government(self) -> None:
        assert decode("DGZTGB") == (
            "Debt Instruments | Mortgage-Backed Securities"
            " | Zero Rate/Discounted | Government/State Guarantee"
            " | Fixed Maturity with Call Feature | Bearer"
        )

    def test_variable_unsecured_amortization(self) -> None:
        assert decode("DGVUAN") == (
            "Debt Instruments | Mortgage-Backed Securities"
            " | Variable | Unsecured/Unguaranteed | Amortization Plan"
            " | Bearer/Registered"
        )


class TestDebtABS:
    def test_fixed_secured(self) -> None:
        assert decode("DAFSFR") == (
            "Debt Instruments | Asset-Backed Securities"
            " | Fixed Rate | Secured | Fixed Maturity | Registered"
        )

    def test_variable_perpetual(self) -> None:
        assert decode("DAVSPB") == (
            "Debt Instruments | Asset-Backed Securities"
            " | Variable | Secured | Perpetual | Bearer"
        )


class TestDebtMunicipalBonds:
    def test_fixed_secured(self) -> None:
        assert decode("DNFSFR") == (
            "Debt Instruments | Municipal Bonds"
            " | Fixed Rate | Secured | Fixed Maturity | Registered"
        )

    def test_zero_government_extendible(self) -> None:
        assert decode("DNZTEM") == (
            "Debt Instruments | Municipal Bonds"
            " | Zero Rate/Discounted | Government/State Guarantee"
            " | Extendible | Others"
        )


class TestDebtDepositoryReceipts:
    def test_bonds_fixed_secured(self) -> None:
        assert decode("DDBFSF") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Bonds | Fixed Rate | Secured | Fixed Maturity"
        )

    def test_convertible_bonds_variable(self) -> None:
        assert decode("DDCVUF") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Convertible Bonds | Variable | Unsecured/Unguaranteed"
            " | Fixed Maturity"
        )

    def test_bonds_with_warrants(self) -> None:
        assert decode("DDWZSF") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Bonds with Warrants | Zero Rate/Discounted | Secured"
            " | Fixed Maturity"
        )

    def test_medium_term_notes(self) -> None:
        assert decode("DDTFNF") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Medium-Term Notes | Fixed Rate | Senior | Fixed Maturity"
        )

    def test_money_market_instruments(self) -> None:
        assert decode("DDYCTA") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Money Market Instruments | Cash Payment"
            " | Government/State Guarantee | Amortization Plan"
        )

    def test_mbs(self) -> None:
        assert decode("DDGFSA") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Mortgage-Backed Securities | Fixed Rate | Secured"
            " | Amortization Plan"
        )

    def test_abs(self) -> None:
        assert decode("DDQVGP") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Asset-Backed Securities | Variable | Joint Guarantee"
            " | Perpetual"
        )

    def test_municipal_bonds(self) -> None:
        assert decode("DDNFSE") == (
            "Debt Instruments | Depository Receipts on Debt Instruments"
            " | Municipal Bonds | Fixed Rate | Secured | Extendible"
        )


class TestDebtMoneyMarket:
    def test_fixed_secured(self) -> None:
        assert decode("DYFSXB") == (
            "Debt Instruments | Money Market Instruments"
            " | Fixed Rate | Secured | Not Applicable/Undefined | Bearer"
        )

    def test_zero_government(self) -> None:
        assert decode("DYZTXR") == (
            "Debt Instruments | Money Market Instruments"
            " | Zero Rate/Discounted | Government/State Guarantee"
            " | Not Applicable/Undefined | Registered"
        )

    def test_variable_unsecured(self) -> None:
        assert decode("DYVUXN") == (
            "Debt Instruments | Money Market Instruments"
            " | Variable | Unsecured/Unguaranteed"
            " | Not Applicable/Undefined | Bearer/Registered"
        )

    def test_payment_in_kind(self) -> None:
        assert decode("DYKNXB") == (
            "Debt Instruments | Money Market Instruments"
            " | Payment in Kind | Senior"
            " | Not Applicable/Undefined | Bearer"
        )


class TestDebtMisc:
    def test_bank_loan(self) -> None:
        assert decode("DMBXXR") == (
            "Debt Instruments | Others (Miscellaneous)"
            " | Bank Loan | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Registered"
        )

    def test_promissory_note(self) -> None:
        assert decode("DMPXXB") == (
            "Debt Instruments | Others (Miscellaneous)"
            " | Promissory Note | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Bearer"
        )

    def test_others(self) -> None:
        assert decode("DMMXXN") == (
            "Debt Instruments | Others (Miscellaneous)"
            " | Others | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Bearer/Registered"
        )


# ---------------------------------------------------------------------------
# C - Collective Investment Vehicles
# ---------------------------------------------------------------------------


class TestCIVStandardFunds:
    def test_open_end_income_equities_shares(self) -> None:
        assert decode("CIOIES") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Income Funds | Equities | Shares"
        )

    def test_closed_end_accumulation_debt(self) -> None:
        assert decode("CICGBU") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Closed-End | Accumulation Funds | Debt Instruments | Units"
        )

    def test_others_mixed_convertible(self) -> None:
        assert decode("CIMJVQ") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Others | Mixed Funds | Convertible Securities"
            " | Shares for Qualified Investors"
        )

    def test_real_estate(self) -> None:
        assert decode("CIOIRY") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Income Funds | Real Estate"
            " | Units for Qualified Investors"
        )

    def test_mixed_assets(self) -> None:
        assert decode("CIOGLS") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Accumulation Funds | Mixed | Shares"
        )

    def test_commodities(self) -> None:
        assert decode("CIOICU") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Income Funds | Commodities | Units"
        )

    def test_derivatives(self) -> None:
        assert decode("CIOIDS") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Income Funds | Derivatives | Shares"
        )

    def test_referential_instruments(self) -> None:
        assert decode("CIOIFS") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Income Funds | Referential Instruments | Shares"
        )

    def test_credits(self) -> None:
        assert decode("CIOIKS") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Income Funds | Credits | Shares"
        )

    def test_others_asset(self) -> None:
        assert decode("CIOIMU") == (
            "Collective Investment Vehicles"
            " | Standard Investment Funds/Mutual Funds"
            " | Open-End | Income Funds | Others | Units"
        )


class TestCIVHedgeFunds:
    def test_shares(self) -> None:
        assert decode("CHXXXS") == (
            "Collective Investment Vehicles | Hedge Funds"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Shares"
        )

    def test_units_qualified(self) -> None:
        assert decode("CHXXXY") == (
            "Collective Investment Vehicles | Hedge Funds"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Units for Qualified Investors"
        )


class TestCIVREITs:
    def test_basic(self) -> None:
        assert decode("CBXXXU") == (
            "Collective Investment Vehicles"
            " | Real Estate Investment Trusts (REITs)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Units"
        )


class TestCIVETFs:
    def test_units(self) -> None:
        assert decode("CEXXXU") == (
            "Collective Investment Vehicles"
            " | Exchange-Traded Funds (ETFs)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Units"
        )

    def test_shares_qualified(self) -> None:
        assert decode("CEXXXQ") == (
            "Collective Investment Vehicles"
            " | Exchange-Traded Funds (ETFs)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Shares for Qualified Investors"
        )


class TestCIVPensionFunds:
    def test_basic(self) -> None:
        assert decode("CSXXXS") == (
            "Collective Investment Vehicles | Pension Funds"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Shares"
        )


class TestCIVFundsOfFunds:
    def test_basic(self) -> None:
        assert decode("CFXXXU") == (
            "Collective Investment Vehicles | Funds of Funds"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Units"
        )


class TestCIVPrivateEquity:
    def test_basic(self) -> None:
        assert decode("CPXXXS") == (
            "Collective Investment Vehicles | Private Equity Funds"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Shares"
        )


class TestCIVEntitlements:
    def test_allotment_rights(self) -> None:
        assert decode("CRAXXB") == (
            "Collective Investment Vehicles | Entitlements (Rights)"
            " | Allotment (Bonus) Rights | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Bearer"
        )

    def test_subscription_rights(self) -> None:
        assert decode("CRSXXR") == (
            "Collective Investment Vehicles | Entitlements (Rights)"
            " | Subscription Rights | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Registered"
        )

    def test_purchase_rights(self) -> None:
        assert decode("CRPXXN") == (
            "Collective Investment Vehicles | Entitlements (Rights)"
            " | Purchase Rights | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Bearer/Registered"
        )

    def test_warrants(self) -> None:
        assert decode("CRWXXR") == (
            "Collective Investment Vehicles | Entitlements (Rights)"
            " | Warrants | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Registered"
        )

    def test_mini_future_certificates(self) -> None:
        assert decode("CRFXXB") == (
            "Collective Investment Vehicles | Entitlements (Rights)"
            " | Mini-Future Certificates/Constant Leverage Certificates"
            " | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Bearer"
        )

    def test_depository_receipts(self) -> None:
        assert decode("CRDXXM") == (
            "Collective Investment Vehicles | Entitlements (Rights)"
            " | Depository Receipts on Entitlements"
            " | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Others"
        )

    def test_others(self) -> None:
        assert decode("CRMXXB") == (
            "Collective Investment Vehicles | Entitlements (Rights)"
            " | Others | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Bearer"
        )


class TestCIVMisc:
    def test_basic(self) -> None:
        assert decode("CMXXXS") == (
            "Collective Investment Vehicles | Others (Miscellaneous)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Shares"
        )


# ---------------------------------------------------------------------------
# O - Listed Options
# ---------------------------------------------------------------------------


class TestListedOptionsCall:
    def test_american_stock_cash_standardized(self) -> None:
        assert decode("OCASCS") == (
            "Listed Options | Call Options"
            " | American | Stock-Equities | Cash | Standardized"
        )

    def test_european_debt_physical_non_standardized(self) -> None:
        assert decode("OCEDPN") == (
            "Listed Options | Call Options"
            " | European | Debt Instruments | Physical | Non-Standardized"
        )

    def test_bermudan_baskets_non_deliverable(self) -> None:
        assert decode("OCBBNS") == (
            "Listed Options | Call Options"
            " | Bermudan | Baskets | Non-Deliverable | Standardized"
        )

    def test_commodities_elect(self) -> None:
        assert decode("OCATES") == (
            "Listed Options | Call Options"
            " | American | Commodities | Elect at Exercise | Standardized"
        )

    def test_currencies(self) -> None:
        assert decode("OCACCS") == (
            "Listed Options | Call Options"
            " | American | Currencies | Cash | Standardized"
        )

    def test_indices(self) -> None:
        assert decode("OCAICS") == (
            "Listed Options | Call Options | American | Indices | Cash | Standardized"
        )

    def test_options_underlying(self) -> None:
        assert decode("OCAOCS") == (
            "Listed Options | Call Options | American | Options | Cash | Standardized"
        )

    def test_futures_underlying(self) -> None:
        assert decode("OCAFCS") == (
            "Listed Options | Call Options | American | Futures | Cash | Standardized"
        )

    def test_swaps_underlying(self) -> None:
        assert decode("OCAWCS") == (
            "Listed Options | Call Options | American | Swaps | Cash | Standardized"
        )

    def test_interest_rates_underlying(self) -> None:
        assert decode("OCANCS") == (
            "Listed Options | Call Options"
            " | American | Interest Rates | Cash | Standardized"
        )

    def test_others_underlying(self) -> None:
        assert decode("OCAMCS") == (
            "Listed Options | Call Options | American | Others | Cash | Standardized"
        )


class TestListedOptionsPut:
    def test_european_debt_physical(self) -> None:
        assert decode("OPEDPN") == (
            "Listed Options | Put Options"
            " | European | Debt Instruments | Physical | Non-Standardized"
        )

    def test_american_stock_cash(self) -> None:
        assert decode("OPASCS") == (
            "Listed Options | Put Options"
            " | American | Stock-Equities | Cash | Standardized"
        )

    def test_bermudan_indices(self) -> None:
        assert decode("OPBICN") == (
            "Listed Options | Put Options"
            " | Bermudan | Indices | Cash | Non-Standardized"
        )


class TestListedOptionsMisc:
    def test_all_x(self) -> None:
        assert decode("OMXXXX") == (
            "Listed Options | Others (Miscellaneous)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# F - Futures
# ---------------------------------------------------------------------------


class TestFuturesFinancial:
    def test_baskets_physical(self) -> None:
        assert decode("FFBPSX") == (
            "Futures | Financial Futures"
            " | Baskets | Physical | Standardized | Not Applicable/Undefined"
        )

    def test_stock_cash(self) -> None:
        assert decode("FFSCSX") == (
            "Futures | Financial Futures"
            " | Stock-Equities | Cash | Standardized"
            " | Not Applicable/Undefined"
        )

    def test_debt_instruments(self) -> None:
        assert decode("FFDCNX") == (
            "Futures | Financial Futures"
            " | Debt Instruments | Cash | Non-Standardized"
            " | Not Applicable/Undefined"
        )

    def test_currencies(self) -> None:
        assert decode("FFCCSX") == (
            "Futures | Financial Futures"
            " | Currencies | Cash | Standardized | Not Applicable/Undefined"
        )

    def test_indices(self) -> None:
        assert decode("FFICSX") == (
            "Futures | Financial Futures"
            " | Indices | Cash | Standardized | Not Applicable/Undefined"
        )

    def test_options_underlying(self) -> None:
        assert decode("FFOCSX") == (
            "Futures | Financial Futures"
            " | Options | Cash | Standardized | Not Applicable/Undefined"
        )

    def test_futures_underlying(self) -> None:
        assert decode("FFFCSX") == (
            "Futures | Financial Futures"
            " | Futures | Cash | Standardized | Not Applicable/Undefined"
        )

    def test_swaps(self) -> None:
        assert decode("FFWCSX") == (
            "Futures | Financial Futures"
            " | Swaps | Cash | Standardized | Not Applicable/Undefined"
        )

    def test_interest_rates(self) -> None:
        assert decode("FFNCSX") == (
            "Futures | Financial Futures"
            " | Interest Rates | Cash | Standardized"
            " | Not Applicable/Undefined"
        )

    def test_stock_dividend(self) -> None:
        assert decode("FFVCSX") == (
            "Futures | Financial Futures"
            " | Stock Dividend | Cash | Standardized"
            " | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("FFMNSX") == (
            "Futures | Financial Futures"
            " | Others | Non-Deliverable | Standardized"
            " | Not Applicable/Undefined"
        )


class TestFuturesCommodities:
    def test_extraction_cash(self) -> None:
        assert decode("FCECSX") == (
            "Futures | Commodities Futures"
            " | Extraction Resources | Cash | Standardized"
            " | Not Applicable/Undefined"
        )

    def test_agriculture_physical(self) -> None:
        assert decode("FCAPSX") == (
            "Futures | Commodities Futures"
            " | Agriculture | Physical | Standardized"
            " | Not Applicable/Undefined"
        )

    def test_industrial_products(self) -> None:
        assert decode("FCICNX") == (
            "Futures | Commodities Futures"
            " | Industrial Products | Cash | Non-Standardized"
            " | Not Applicable/Undefined"
        )

    def test_services(self) -> None:
        assert decode("FCSCSX") == (
            "Futures | Commodities Futures"
            " | Services | Cash | Standardized | Not Applicable/Undefined"
        )

    def test_environmental(self) -> None:
        assert decode("FCNCSX") == (
            "Futures | Commodities Futures"
            " | Environmental | Cash | Standardized | Not Applicable/Undefined"
        )

    def test_polypropylene(self) -> None:
        assert decode("FCPCSX") == (
            "Futures | Commodities Futures"
            " | Polypropylene Products | Cash | Standardized"
            " | Not Applicable/Undefined"
        )

    def test_generated_resources(self) -> None:
        assert decode("FCHCSX") == (
            "Futures | Commodities Futures"
            " | Generated Resources | Cash | Standardized"
            " | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("FCMNSX") == (
            "Futures | Commodities Futures"
            " | Others | Non-Deliverable | Standardized"
            " | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# H - Non-Listed and Complex Listed Options
# ---------------------------------------------------------------------------


class TestNonListedOptions:
    def test_rates(self) -> None:
        assert decode("HRXXXX") == (
            "Non-Listed and Complex Listed Options | Rates"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_commodities(self) -> None:
        assert decode("HTXXXX") == (
            "Non-Listed and Complex Listed Options | Commodities"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_equity(self) -> None:
        assert decode("HEXXXX") == (
            "Non-Listed and Complex Listed Options | Equity"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_credit(self) -> None:
        assert decode("HCXXXX") == (
            "Non-Listed and Complex Listed Options | Credit"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_fx(self) -> None:
        assert decode("HFXXXX") == (
            "Non-Listed and Complex Listed Options | Foreign Exchange"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("HMXXXX") == (
            "Non-Listed and Complex Listed Options | Others (Miscellaneous)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# I - Spots
# ---------------------------------------------------------------------------


class TestSpots:
    def test_fx(self) -> None:
        assert decode("IFXXXP") == (
            "Spots | Foreign Exchange"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Physical"
        )

    def test_commodities_agriculture(self) -> None:
        assert decode("ITAXXX") == (
            "Spots | Commodities | Agriculture"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities_energy(self) -> None:
        assert decode("ITJXXX") == (
            "Spots | Commodities | Energy"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities_metals(self) -> None:
        assert decode("ITKXXX") == (
            "Spots | Commodities | Metals"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities_environmental(self) -> None:
        assert decode("ITNXXX") == (
            "Spots | Commodities | Environmental"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities_polypropylene(self) -> None:
        assert decode("ITPXXX") == (
            "Spots | Commodities | Polypropylene Products"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities_fertilizer(self) -> None:
        assert decode("ITSXXX") == (
            "Spots | Commodities | Fertilizer"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities_paper(self) -> None:
        assert decode("ITTXXX") == (
            "Spots | Commodities | Paper"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities_others(self) -> None:
        assert decode("ITMXXX") == (
            "Spots | Commodities | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# J - Forwards
# ---------------------------------------------------------------------------


class TestForwards:
    def test_equity(self) -> None:
        assert decode("JEXXXX") == (
            "Forwards | Equity"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_fx(self) -> None:
        assert decode("JFXXXX") == (
            "Forwards | Foreign Exchange"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_credit(self) -> None:
        assert decode("JCXXXX") == (
            "Forwards | Credit"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_rates(self) -> None:
        assert decode("JRXXXX") == (
            "Forwards | Rates"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_commodities(self) -> None:
        assert decode("JTXXXX") == (
            "Forwards | Commodities"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# K - Strategies
# ---------------------------------------------------------------------------


class TestStrategies:
    def test_rates(self) -> None:
        assert decode("KRXXXX") == (
            "Strategies | Rates"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_commodities(self) -> None:
        assert decode("KTXXXX") == (
            "Strategies | Commodities"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_equity(self) -> None:
        assert decode("KEXXXX") == (
            "Strategies | Equity"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_credit(self) -> None:
        assert decode("KCXXXX") == (
            "Strategies | Credit"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_fx(self) -> None:
        assert decode("KFXXXX") == (
            "Strategies | Foreign Exchange"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_mixed_assets(self) -> None:
        assert decode("KYXXXX") == (
            "Strategies | Mixed Assets"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("KMXXXX") == (
            "Strategies | Others (Miscellaneous)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# L - Financing
# ---------------------------------------------------------------------------


class TestFinancingLoanLease:
    def test_agriculture_physical(self) -> None:
        assert decode("LLAXXP") == (
            "Financing | Loan Lease | Agriculture"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Physical"
        )

    def test_baskets_cash(self) -> None:
        assert decode("LLBXXC") == (
            "Financing | Loan Lease | Baskets"
            " | Not Applicable/Undefined | Not Applicable/Undefined | Cash"
        )

    def test_energy_non_deliverable(self) -> None:
        assert decode("LLJXXN") == (
            "Financing | Loan Lease | Energy"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Non-Deliverable"
        )

    def test_metals(self) -> None:
        assert decode("LLKXXP") == (
            "Financing | Loan Lease | Metals"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Physical"
        )

    def test_environmental(self) -> None:
        assert decode("LLNXXC") == (
            "Financing | Loan Lease | Environmental"
            " | Not Applicable/Undefined | Not Applicable/Undefined | Cash"
        )

    def test_polypropylene(self) -> None:
        assert decode("LLPXXP") == (
            "Financing | Loan Lease | Polypropylene Products"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Physical"
        )

    def test_fertilizer(self) -> None:
        assert decode("LLSXXC") == (
            "Financing | Loan Lease | Fertilizer"
            " | Not Applicable/Undefined | Not Applicable/Undefined | Cash"
        )

    def test_paper(self) -> None:
        assert decode("LLTXXP") == (
            "Financing | Loan Lease | Paper"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Physical"
        )

    def test_others(self) -> None:
        assert decode("LLMXXN") == (
            "Financing | Loan Lease | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Non-Deliverable"
        )


class TestFinancingRepo:
    def test_general_flexible_dvp(self) -> None:
        assert decode("LRGFXD") == (
            "Financing | Repurchase Agreements"
            " | General Collateral | Flexible"
            " | Not Applicable/Undefined | Delivery versus Payment"
        )

    def test_specific_overnight_hold(self) -> None:
        assert decode("LRSNXH") == (
            "Financing | Repurchase Agreements"
            " | Specific Security Collateral | Overnight"
            " | Not Applicable/Undefined | Hold-in-Custody"
        )

    def test_cash_open_tri_party(self) -> None:
        assert decode("LRCOXT") == (
            "Financing | Repurchase Agreements"
            " | Cash Collateral | Open"
            " | Not Applicable/Undefined | Tri-Party"
        )

    def test_term(self) -> None:
        assert decode("LRGTXD") == (
            "Financing | Repurchase Agreements"
            " | General Collateral | Term"
            " | Not Applicable/Undefined | Delivery versus Payment"
        )


class TestFinancingSecuritiesLending:
    def test_cash_open_dvp(self) -> None:
        assert decode("LSCOXD") == (
            "Financing | Securities Lending"
            " | Cash Collateral | Open"
            " | Not Applicable/Undefined | Delivery versus Payment"
        )

    def test_govt_bonds_overnight_free(self) -> None:
        assert decode("LSGNXF") == (
            "Financing | Securities Lending"
            " | Government Bonds | Overnight"
            " | Not Applicable/Undefined | Free of Payment"
        )

    def test_corporate_bonds_term_hold(self) -> None:
        assert decode("LSPTXH") == (
            "Financing | Securities Lending"
            " | Corporate Bonds | Term"
            " | Not Applicable/Undefined | Hold-in-Custody"
        )

    def test_convertible_bonds_tri_party(self) -> None:
        assert decode("LSTOXT") == (
            "Financing | Securities Lending"
            " | Convertible Bonds | Open"
            " | Not Applicable/Undefined | Tri-Party"
        )

    def test_equity(self) -> None:
        assert decode("LSETXD") == (
            "Financing | Securities Lending"
            " | Equity | Term"
            " | Not Applicable/Undefined | Delivery versus Payment"
        )

    def test_letter_of_credit(self) -> None:
        assert decode("LSLNXD") == (
            "Financing | Securities Lending"
            " | Letter of Credit | Overnight"
            " | Not Applicable/Undefined | Delivery versus Payment"
        )

    def test_certificate_of_deposit(self) -> None:
        assert decode("LSDOXF") == (
            "Financing | Securities Lending"
            " | Certificate of Deposit | Open"
            " | Not Applicable/Undefined | Free of Payment"
        )

    def test_warrants(self) -> None:
        assert decode("LSWTXH") == (
            "Financing | Securities Lending"
            " | Warrants | Term"
            " | Not Applicable/Undefined | Hold-in-Custody"
        )

    def test_money_market(self) -> None:
        assert decode("LSKNXD") == (
            "Financing | Securities Lending"
            " | Money Market Instruments | Overnight"
            " | Not Applicable/Undefined | Delivery versus Payment"
        )

    def test_others(self) -> None:
        assert decode("LSMOXF") == (
            "Financing | Securities Lending"
            " | Others | Open"
            " | Not Applicable/Undefined | Free of Payment"
        )


# ---------------------------------------------------------------------------
# T - Referential Instruments
# ---------------------------------------------------------------------------


class TestReferentialCurrencies:
    def test_national(self) -> None:
        assert decode("TCNXXX") == (
            "Referential Instruments | Currencies | National Currency"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_legacy(self) -> None:
        assert decode("TCLXXX") == (
            "Referential Instruments | Currencies | Legacy Currency"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_bullion_coins(self) -> None:
        assert decode("TCCXXX") == (
            "Referential Instruments | Currencies | Bullion Coins"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("TCMXXX") == (
            "Referential Instruments | Currencies | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )


class TestReferentialCommodities:
    def test_extraction(self) -> None:
        assert decode("TTEXXX") == (
            "Referential Instruments | Commodities | Extraction Resources"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_agriculture(self) -> None:
        assert decode("TTAXXX") == (
            "Referential Instruments | Commodities | Agriculture"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_industrial(self) -> None:
        assert decode("TTIXXX") == (
            "Referential Instruments | Commodities | Industrial Products"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_services(self) -> None:
        assert decode("TTSXXX") == (
            "Referential Instruments | Commodities | Services"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_environmental(self) -> None:
        assert decode("TTNXXX") == (
            "Referential Instruments | Commodities | Environmental"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_polypropylene(self) -> None:
        assert decode("TTPXXX") == (
            "Referential Instruments | Commodities | Polypropylene Products"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_generated(self) -> None:
        assert decode("TTHXXX") == (
            "Referential Instruments | Commodities | Generated Resources"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("TTMXXX") == (
            "Referential Instruments | Commodities | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )


class TestReferentialInterestRates:
    def test_nominal_quarterly(self) -> None:
        assert decode("TRNQXX") == (
            "Referential Instruments | Interest Rates"
            " | Nominal | Quarterly"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_variable_daily(self) -> None:
        assert decode("TRVDXX") == (
            "Referential Instruments | Interest Rates"
            " | Variable | Daily"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_fixed_weekly(self) -> None:
        assert decode("TRFWXX") == (
            "Referential Instruments | Interest Rates"
            " | Fixed | Weekly"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_real_monthly(self) -> None:
        assert decode("TRRNXX") == (
            "Referential Instruments | Interest Rates"
            " | Real | Monthly"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_others_semi_annually(self) -> None:
        assert decode("TRMSXX") == (
            "Referential Instruments | Interest Rates"
            " | Others | Semi-Annually"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_annually(self) -> None:
        assert decode("TRNAXX") == (
            "Referential Instruments | Interest Rates"
            " | Nominal | Annually"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )

    def test_others_frequency(self) -> None:
        assert decode("TRNMXX") == (
            "Referential Instruments | Interest Rates"
            " | Nominal | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )


class TestReferentialIndices:
    def test_equities_cap_weighted_price_return(self) -> None:
        assert decode("TIECPX") == (
            "Referential Instruments | Indices"
            " | Equities | Capitalization Weighted | Price Return"
            " | Not Applicable/Undefined"
        )

    def test_debt_price_weighted_net_total(self) -> None:
        assert decode("TIDPNX") == (
            "Referential Instruments | Indices"
            " | Debt | Price Weighted | Net Total Return"
            " | Not Applicable/Undefined"
        )

    def test_civ_equal_weighted_gross_total(self) -> None:
        assert decode("TIFEGX") == (
            "Referential Instruments | Indices"
            " | Collective Investment Vehicles | Equal Weighted"
            " | Gross Total Return | Not Applicable/Undefined"
        )

    def test_real_estate_modified_cap(self) -> None:
        assert decode("TIRFMX") == (
            "Referential Instruments | Indices"
            " | Real Estate | Modified Market Capitalization Weighted"
            " | Others | Not Applicable/Undefined"
        )

    def test_commodities(self) -> None:
        assert decode("TITCPX") == (
            "Referential Instruments | Indices"
            " | Commodities | Capitalization Weighted | Price Return"
            " | Not Applicable/Undefined"
        )

    def test_currencies(self) -> None:
        assert decode("TICMPX") == (
            "Referential Instruments | Indices"
            " | Currencies | Others | Price Return"
            " | Not Applicable/Undefined"
        )

    def test_others_asset(self) -> None:
        assert decode("TIMEPX") == (
            "Referential Instruments | Indices"
            " | Others | Equal Weighted | Price Return"
            " | Not Applicable/Undefined"
        )


class TestReferentialBaskets:
    def test_equities(self) -> None:
        assert decode("TBEXXX") == (
            "Referential Instruments | Baskets | Equities"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_debt(self) -> None:
        assert decode("TBDXXX") == (
            "Referential Instruments | Baskets | Debt"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_civ(self) -> None:
        assert decode("TBFXXX") == (
            "Referential Instruments | Baskets"
            " | Collective Investment Vehicles"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_indices(self) -> None:
        assert decode("TBIXXX") == (
            "Referential Instruments | Baskets | Indices"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_commodities(self) -> None:
        assert decode("TBTXXX") == (
            "Referential Instruments | Baskets | Commodities"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_currencies(self) -> None:
        assert decode("TBCXXX") == (
            "Referential Instruments | Baskets | Currencies"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("TBMXXX") == (
            "Referential Instruments | Baskets | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )


class TestReferentialStockDividends:
    def test_common(self) -> None:
        assert decode("TDSXXX") == (
            "Referential Instruments | Stock Dividends"
            " | Common/Ordinary Shares"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_preferred(self) -> None:
        assert decode("TDPXXX") == (
            "Referential Instruments | Stock Dividends"
            " | Preferred/Preference Shares"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_common_convertible(self) -> None:
        assert decode("TDCXXX") == (
            "Referential Instruments | Stock Dividends"
            " | Common/Ordinary Convertible Shares"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_preferred_convertible(self) -> None:
        assert decode("TDFXXX") == (
            "Referential Instruments | Stock Dividends"
            " | Preferred/Preference Convertible Shares"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_limited_partnership(self) -> None:
        assert decode("TDLXXX") == (
            "Referential Instruments | Stock Dividends"
            " | Limited Partnership Units"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_civ(self) -> None:
        assert decode("TDKXXX") == (
            "Referential Instruments | Stock Dividends"
            " | Collective Investment Vehicles"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("TDMXXX") == (
            "Referential Instruments | Stock Dividends | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )


class TestReferentialMisc:
    def test_all_x(self) -> None:
        assert decode("TMXXXX") == (
            "Referential Instruments | Others (Miscellaneous)"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# M - Others (Miscellaneous)
# ---------------------------------------------------------------------------


class TestMiscCombined:
    def test_shares_free_bearer(self) -> None:
        assert decode("MCSUXB") == (
            "Others (Miscellaneous) | Combined Instruments"
            " | Combination of Shares | Free"
            " | Not Applicable/Undefined | Bearer"
        )

    def test_bonds_restrictions_registered(self) -> None:
        assert decode("MCBTXR") == (
            "Others (Miscellaneous) | Combined Instruments"
            " | Combination of Bonds | Restrictions"
            " | Not Applicable/Undefined | Registered"
        )

    def test_share_and_bond(self) -> None:
        assert decode("MCHUXN") == (
            "Others (Miscellaneous) | Combined Instruments"
            " | Share and Bond | Free"
            " | Not Applicable/Undefined | Bearer/Registered"
        )

    def test_share_and_warrant(self) -> None:
        assert decode("MCAUXM") == (
            "Others (Miscellaneous) | Combined Instruments"
            " | Share and Warrant | Free"
            " | Not Applicable/Undefined | Others"
        )

    def test_warrant_and_warrant(self) -> None:
        assert decode("MCWTXB") == (
            "Others (Miscellaneous) | Combined Instruments"
            " | Warrant and Warrant | Restrictions"
            " | Not Applicable/Undefined | Bearer"
        )

    def test_fund_units(self) -> None:
        assert decode("MCUUXR") == (
            "Others (Miscellaneous) | Combined Instruments"
            " | Fund Units and Other Components | Free"
            " | Not Applicable/Undefined | Registered"
        )

    def test_others_component(self) -> None:
        assert decode("MCMTXB") == (
            "Others (Miscellaneous) | Combined Instruments"
            " | Others | Restrictions"
            " | Not Applicable/Undefined | Bearer"
        )


class TestMiscOthers:
    def test_real_estate_deeds(self) -> None:
        assert decode("MMRXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Real Estate Deeds"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_insurance_policies(self) -> None:
        assert decode("MMIXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Insurance Policies"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_escrow_receipts(self) -> None:
        assert decode("MMEXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Escrow Receipts"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_trade_finance(self) -> None:
        assert decode("MMTXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Trade Finance Instruments"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_carbon_credit(self) -> None:
        assert decode("MMNXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Carbon Credit"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_precious_metal_receipts(self) -> None:
        assert decode("MMPXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Precious Metal Receipts"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_otc_derivatives(self) -> None:
        assert decode("MMSXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Other OTC Derivative Products"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )

    def test_others(self) -> None:
        assert decode("MMMXXX") == (
            "Others (Miscellaneous) | Others (Miscellaneous)"
            " | Others"
            " | Not Applicable/Undefined | Not Applicable/Undefined"
            " | Not Applicable/Undefined"
        )


# ---------------------------------------------------------------------------
# Input handling and error cases
# ---------------------------------------------------------------------------


class TestDecodeInputHandling:
    """Case insensitivity and whitespace handling."""

    def test_lowercase_accepted(self) -> None:
        assert decode("esvufr") == decode("ESVUFR")

    def test_mixed_case(self) -> None:
        assert decode("EsVuFr") == decode("ESVUFR")

    def test_lowercase_all_categories(self) -> None:
        assert decode("dbfsfb") == decode("DBFSFB")
        assert decode("ocascs") == decode("OCASCS")
        assert decode("ffbpsx") == decode("FFBPSX")
        assert decode("hrxxxx") == decode("HRXXXX")

    def test_whitespace_not_stripped(self) -> None:
        with pytest.raises(ValueError, match="6 characters"):
            decode(" ESVUFR")
        with pytest.raises(ValueError, match="6 characters"):
            decode("ESVUFR ")
        with pytest.raises(ValueError, match="6 characters"):
            decode(" ESVUFR ")


class TestDecodeErrors:
    """Error cases raise appropriate exceptions with descriptive messages."""

    def test_empty_string(self) -> None:
        with pytest.raises(ValueError, match="6 characters"):
            decode("")

    def test_too_short_1(self) -> None:
        with pytest.raises(ValueError, match="6 characters"):
            decode("E")

    def test_too_short_5(self) -> None:
        with pytest.raises(ValueError, match="6 characters"):
            decode("ESVUF")

    def test_too_long_7(self) -> None:
        with pytest.raises(ValueError, match="6 characters"):
            decode("ESVUFRX")

    def test_too_long_12(self) -> None:
        with pytest.raises(ValueError, match="6 characters"):
            decode("ESVUFRESVUFR")

    def test_invalid_category(self) -> None:
        with pytest.raises(ValueError, match="Unknown category"):
            decode("ZSVUFR")

    def test_invalid_category_number(self) -> None:
        with pytest.raises(ValueError, match="Unknown category"):
            decode("1SVUFR")

    def test_invalid_group_for_equities(self) -> None:
        with pytest.raises(ValueError, match="Unknown group"):
            decode("EZVUFR")

    def test_invalid_group_for_debt(self) -> None:
        with pytest.raises(ValueError, match="Unknown group"):
            decode("DZFSFB")

    def test_invalid_group_for_options(self) -> None:
        with pytest.raises(ValueError, match="Unknown group"):
            decode("OAXXXX")

    def test_invalid_attribute_pos3(self) -> None:
        with pytest.raises(ValueError, match="position 3"):
            decode("ES9UFR")

    def test_invalid_attribute_pos4(self) -> None:
        with pytest.raises(ValueError, match="position 4"):
            decode("ESV9FR")

    def test_invalid_attribute_pos5(self) -> None:
        with pytest.raises(ValueError, match="position 5"):
            decode("ESVU9R")

    def test_invalid_attribute_pos6(self) -> None:
        with pytest.raises(ValueError, match="position 6"):
            decode("ESVUF9")

    def test_error_message_includes_label(self) -> None:
        with pytest.raises(ValueError, match="Voting Right"):
            decode("ES9UFR")

    def test_non_string_none(self) -> None:
        with pytest.raises(TypeError, match="Expected str"):
            decode(None)  # type: ignore[invalid-argument-type]

    def test_non_string_int(self) -> None:
        with pytest.raises(TypeError, match="Expected str"):
            decode(123)  # type: ignore[invalid-argument-type]

    def test_non_string_bytes(self) -> None:
        with pytest.raises(TypeError, match="Expected str"):
            decode(b"ESVUFR")  # type: ignore[invalid-argument-type]

    def test_non_string_list(self) -> None:
        with pytest.raises(TypeError, match="Expected str"):
            decode(["E", "S", "V", "U", "F", "R"])  # type: ignore[invalid-argument-type]
