from care.emr.resources.encounter.constants import (
    AdmitSourcesChoices,
    DischargeDispositionChoices,
)


def get_admit_source_display(value: str) -> str:  # noqa: PLR0911
    match value:
        case AdmitSourcesChoices.hosp_trans.value:
            return "Transferred from other hospital"
        case AdmitSourcesChoices.emd.value:
            return "From accident/emergency department"
        case AdmitSourcesChoices.outp.value:
            return "From outpatient department"
        case AdmitSourcesChoices.born.value:
            return "Born in hospital"
        case AdmitSourcesChoices.gp.value:
            return "General Practitioner referral"
        case AdmitSourcesChoices.mp.value:
            return "Medical Practitioner/physician referral"
        case AdmitSourcesChoices.nursing.value:
            return "From nursing home"
        case AdmitSourcesChoices.psych.value:
            return "From psychiatric hospital"
        case AdmitSourcesChoices.rehab.value:
            return "From rehabilitation facility"
        case AdmitSourcesChoices.other.value:
            return "Other"
        case _:
            return "Unknown"


def get_discharge_disposition_display(value: str) -> str:  # noqa: PLR0911
    match value:
        case DischargeDispositionChoices.home.value:
            return "Home"
        case DischargeDispositionChoices.alt_home.value:
            return "Alternate Home"
        case DischargeDispositionChoices.other_hcf.value:
            return "Other Health Care Facility"
        case DischargeDispositionChoices.hosp.value:
            return "Hospital"
        case DischargeDispositionChoices.long.value:
            return "Long-term Care Facility"
        case DischargeDispositionChoices.aadvice.value:
            return "Against Medical Advice"
        case DischargeDispositionChoices.exp.value:
            return "Expired"
        case DischargeDispositionChoices.psy.value:
            return "Psychiatric Hospital"
        case DischargeDispositionChoices.rehab.value:
            return "Rehabilitation Facility"
        case DischargeDispositionChoices.snf.value:
            return "Skilled Nursing Facility"
        case DischargeDispositionChoices.oth.value:
            return "Other"
        case _:
            return "N/A"
