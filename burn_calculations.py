"""Input and validation helpers for the fictional BurnFluid console app.

This module contains patient prompts and validation only.  It does not
calculate IV fluids and is not intended for real clinical use.
"""

import math
import re


EDUCATIONAL_DISCLAIMER = (
    "EDUCATIONAL USE ONLY: This fictional patient tool is for learning and "
    "demonstration only. It is not a substitute for professional medical "
    "assessment or clinical advice."
)

EMIRATES_ID_PATTERN = re.compile(r"^784-0000-[0-9]{7}-[0-9]$")


def print_educational_disclaimer():
    """Print a clear disclaimer before any patient information is collected."""
    print(EDUCATIONAL_DISCLAIMER)


def validate_emirates_id(emirates_id):
    """Return a stripped ID if it is in the fixed fictional 784-0000 format."""
    if not isinstance(emirates_id, str):
        raise ValueError("Emirates ID must be text.")

    emirates_id = emirates_id.strip()
    if not EMIRATES_ID_PATTERN.fullmatch(emirates_id):
        raise ValueError(
            "Emirates ID must use the format 784-0000-0000001-0."
        )
    return emirates_id


def validate_patient_name(patient_name):
    """Return a stripped patient name if it is not empty."""
    if not isinstance(patient_name, str):
        raise ValueError("Patient name must be text.")

    patient_name = patient_name.strip()
    if patient_name == "":
        raise ValueError("Patient name cannot be empty.")
    return patient_name


def validate_patient_age(patient_age):
    """Return an integer age when it is from 18 through 120."""
    if isinstance(patient_age, bool):
        raise ValueError("Age must be a whole number.")

    try:
        age_text = str(patient_age).strip()
        if not re.fullmatch(r"[+-]?\d+", age_text):
            raise ValueError("Age must be a whole number.")
        age = int(age_text)
    except (TypeError, ValueError, OverflowError):
        raise ValueError("Age must be a whole number.")

    if age < 18 or age > 120:
        raise ValueError("Age must be between 18 and 120.")
    return age


def validate_finite_number(value, field_name):
    """Convert a value to float and reject NaN or infinity values."""
    if isinstance(value, bool):
        raise ValueError(field_name + " must be a number.")

    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(field_name + " must be a number.")

    if not math.isfinite(number):
        raise ValueError(field_name + " must be a finite number.")
    return number


def validate_patient_weight(patient_weight_kg):
    """Return weight in kg if it is from 30 through 250."""
    weight = validate_finite_number(patient_weight_kg, "Weight")
    if weight < 30 or weight > 250:
        raise ValueError("Weight must be between 30 and 250 kg.")
    return weight


def validate_tbsa(tbsa_percent):
    """Return TBSA as a percentage if it is from 20 through 100."""
    tbsa = validate_finite_number(tbsa_percent, "TBSA")
    if tbsa < 20 or tbsa > 100:
        raise ValueError("TBSA must be between 20 and 100 percent.")
    return tbsa


def validate_hours_since_burn(hours_since_burn):
    """Return hours since the burn, not since hospital arrival.

    Valid injury time is from 0 hours (inclusive) up to, but not including,
    24 hours.
    """
    hours = validate_finite_number(
        hours_since_burn, "Hours since the burn injury"
    )
    if hours < 0 or hours >= 24:
        raise ValueError(
            "Hours since burn injury must be 0 or more and less than 24."
        )
    return hours


def validate_fluid_given(fluid_given_ml):
    """Return fluid received during the selected phase in ml, if non-negative.

    This is the amount received during the selected fluid phase.  It is not
    necessarily the cumulative volume received since the burn injury.
    """
    fluid_volume = validate_finite_number(
        fluid_given_ml, "Fluid received during the selected phase"
    )
    if fluid_volume < 0:
        raise ValueError(
            "Fluid received during the selected phase cannot be negative."
        )
    return fluid_volume


def validate_fluid_phase(fluid_phase):
    """Normalize and validate the selected resuscitation phase."""
    if not isinstance(fluid_phase, str):
        raise ValueError("Fluid phase must be text.")

    fluid_phase = fluid_phase.strip().lower()
    valid_phases = ("first_8h", "next_16h", "unknown")
    if fluid_phase not in valid_phases:
        raise ValueError(
            "Fluid phase must be first_8h, next_16h, or unknown."
        )
    return fluid_phase


def validate_inhalation_injury(inhalation_injury):
    """Convert Y/N text (or Boolean text) to a Boolean."""
    if isinstance(inhalation_injury, bool):
        return inhalation_injury

    if not isinstance(inhalation_injury, str):
        raise ValueError("Inhalation injury must be Y or N.")

    answer = inhalation_injury.strip().lower()
    if answer == "y":
        return True
    if answer == "n":
        return False
    raise ValueError("Inhalation injury must be Y or N.")


def prompt_text(prompt):
    """Prompt for text and return None if Ctrl+C or EOF cancels input."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nPatient data collection cancelled.")
        return None


def get_valid_emirates_id():
    """Repeat the Emirates ID prompt until it passes validation."""
    while True:
        answer = prompt_text(
            "Fictional Emirates ID (784-0000-0000001-0): "
        )
        if answer is None:
            return None
        try:
            return validate_emirates_id(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_patient_name():
    """Repeat the patient name prompt until it is non-empty."""
    while True:
        answer = prompt_text("Fictional patient name: ")
        if answer is None:
            return None
        try:
            return validate_patient_name(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_patient_age():
    """Repeat the age prompt until a whole number from 18 to 120 is entered."""
    while True:
        answer = prompt_text("Patient age (18-120): ")
        if answer is None:
            return None
        try:
            return validate_patient_age(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_patient_weight():
    """Repeat the weight prompt until 30 through 250 kg is entered."""
    while True:
        answer = prompt_text("Patient weight in kg (30-250): ")
        if answer is None:
            return None
        try:
            return validate_patient_weight(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_tbsa():
    """Repeat the TBSA prompt until 20 through 100 percent is entered."""
    while True:
        answer = prompt_text("TBSA burn percentage (20-100): ")
        if answer is None:
            return None
        try:
            return validate_tbsa(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_hours_since_burn():
    """Repeat the injury-time prompt until a value from 0 to under 24."""
    while True:
        answer = prompt_text(
            "Hours since burn injury (0 to less than 24): "
        )
        if answer is None:
            return None
        try:
            return validate_hours_since_burn(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_fluid_given():
    """Repeat until the phase fluid volume is finite and non-negative."""
    while True:
        answer = prompt_text(
            "Fluid received during the selected phase in ml "
            "(0 or greater): "
        )
        if answer is None:
            return None
        try:
            return validate_fluid_given(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_fluid_phase():
    """Repeat the phase prompt until a supported value is entered."""
    while True:
        answer = prompt_text(
            "Fluid phase (first_8h, next_16h, or unknown): "
        )
        if answer is None:
            return None
        try:
            return validate_fluid_phase(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_inhalation_injury():
    """Repeat the inhalation prompt until Y or N is entered."""
    while True:
        answer = prompt_text("Inhalation injury (Y/N): ")
        if answer is None:
            return None
        try:
            return validate_inhalation_injury(answer)
        except ValueError as error:
            print("Invalid input:", error)


def collect_patient_data():
    """Prompt for, validate, and return one fictional patient dictionary."""
    print_educational_disclaimer()

    emirates_id = get_valid_emirates_id()
    if emirates_id is None:
        return None

    patient_name = get_valid_patient_name()
    if patient_name is None:
        return None

    patient_age = get_valid_patient_age()
    if patient_age is None:
        return None

    patient_weight_kg = get_valid_patient_weight()
    if patient_weight_kg is None:
        return None

    tbsa_percent = get_valid_tbsa()
    if tbsa_percent is None:
        return None

    hours_since_burn = get_valid_hours_since_burn()
    if hours_since_burn is None:
        return None

    fluid_given_ml = get_valid_fluid_given()
    if fluid_given_ml is None:
        return None

    fluid_phase = get_valid_fluid_phase()
    if fluid_phase is None:
        return None

    inhalation_injury = get_valid_inhalation_injury()
    if inhalation_injury is None:
        return None

    return {
        "emirates_id": emirates_id,
        "patient_name": patient_name,
        "patient_age": patient_age,
        "patient_weight_kg": patient_weight_kg,
        "tbsa_percent": tbsa_percent,
        "hours_since_burn": hours_since_burn,
        "fluid_given_ml": fluid_given_ml,
        "fluid_phase": fluid_phase,
        "inhalation_injury": inhalation_injury,
    }


if __name__ == "__main__":
    patient = collect_patient_data()
    if patient is not None:
        print("\nValidated patient data:")
        for key, value in patient.items():
            print(key + ":", value)