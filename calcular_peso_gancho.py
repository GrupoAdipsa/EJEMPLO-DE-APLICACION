"""Herramienta para estimar el peso de un gancho de estribo.

El peso se calcula multiplicando la longitud teórica del gancho por el
peso lineal de la barra de acero (densidad 7 850 kg/m³). La longitud del
gancho se aproxima como la suma de:

* Dos tramos rectos con la separación libre entre la barra longitudinal
  y el estribo.
* Una semicircunferencia cuyo radio equivale a la distancia entre los
  ejes del estribo y la barra longitudinal.

Todas las dimensiones se introducen en milímetros y el resultado se
entrega en kilogramos.
"""

from __future__ import annotations

import argparse
import math

DENSIDAD_ACERO = 7_850  # kg/m^3


def peso_lineal_barra(diametro_mm: float) -> float:
    """Calcula el peso lineal (kg/m) de una barra en función de su diámetro."""

    diametro_m = diametro_mm / 1_000
    area_m2 = math.pi * (diametro_m**2) / 4
    return area_m2 * DENSIDAD_ACERO


def longitud_gancho(
    diametro_estribo_mm: float,
    distancia_libre_mm: float,
    diametro_barra_longitudinal_mm: float,
) -> float:
    """Devuelve la longitud del gancho en metros."""

    # Tramos rectos que unen el eje del estribo con el inicio del doblez
    longitud_recta_mm = 2 * distancia_libre_mm

    # Longitud del doblez semicircular medida en el eje del estribo
    radio_equivalente_mm = (diametro_estribo_mm + diametro_barra_longitudinal_mm) / 2
    longitud_curva_mm = math.pi * radio_equivalente_mm

    return (longitud_recta_mm + longitud_curva_mm) / 1_000


def calcular_peso_gancho(
    diametro_estribo_mm: float,
    distancia_libre_mm: float,
    diametro_barra_longitudinal_mm: float,
) -> float:
    """Calcula el peso total del gancho del estribo en kilogramos."""

    longitud = longitud_gancho(
        diametro_estribo_mm, distancia_libre_mm, diametro_barra_longitudinal_mm
    )
    peso_lineal = peso_lineal_barra(diametro_estribo_mm)
    return longitud * peso_lineal


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Calcula el peso aproximado del gancho de un estribo a partir del "
            "diámetro del estribo, el diámetro de la barra longitudinal y la "
            "separación libre entre ambos."
        )
    )
    parser.add_argument(
        "diametro_estribo",
        type=float,
        help="Diámetro del estribo en milímetros",
    )
    parser.add_argument(
        "diametro_barra_longitudinal",
        type=float,
        help="Diámetro de la barra longitudinal en milímetros",
    )
    parser.add_argument(
        "distancia_libre",
        type=float,
        help=(
            "Distancia libre (en milímetros) entre la cara exterior de la barra "
            "longitudinal y el eje del estribo antes del gancho"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    peso = calcular_peso_gancho(
        args.diametro_estribo,
        args.distancia_libre,
        args.diametro_barra_longitudinal,
    )
    print(
        (
            "Peso del gancho: {peso:.4f} kg (longitud = {longitud:.3f} m, "
            "peso lineal = {peso_lineal:.3f} kg/m)"
        ).format(
            peso=peso,
            longitud=longitud_gancho(
                args.diametro_estribo,
                args.distancia_libre,
                args.diametro_barra_longitudinal,
            ),
            peso_lineal=peso_lineal_barra(args.diametro_estribo),
        )
    )


if __name__ == "__main__":
    main()
