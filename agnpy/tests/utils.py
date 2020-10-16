# utils for the test scripts
import matplotlib.pyplot as plt


def make_sed_comparison_plot(
    nu,
    reference_sed,
    comparison_sed,
    reference_label,
    comparison_label,
    fig_title,
    fig_path,
):
    """make a SED comparison plot for visual inspection"""
    fig, ax = plt.subplots(
        2, sharex=True, gridspec_kw={"height_ratios": [2, 1]}, figsize=(8, 6)
    )
    # plot the SEDs in the upper panel
    ax[0].loglog(nu, reference_sed, marker="o", ls="-", lw=1.5, label=reference_label)
    ax[0].loglog(
        nu, comparison_sed, marker=".", ls="--", lw=1.5, label=comparison_label
    )
    ax[0].legend()
    ax[0].set_xlabel(r"$\nu\,/\,{\rm Hz}$")
    ax[0].set_ylabel(r"$\nu F_{\nu}\,/\,({\rm erg}\,{\rm cm}^{-2}\,{\rm s}^{-1})$")
    ax[0].set_title(fig_title)
    # plot the deviation in the bottom panel
    deviation = 1 - comparison_sed / reference_sed
    ax[1].axhline(0, ls="-", color="darkgray")
    ax[1].axhline(0.2, ls="--", color="darkgray")
    ax[1].axhline(-0.2, ls="--", color="darkgray")
    ax[1].axhline(0.3, ls=":", color="darkgray")
    ax[1].axhline(-0.3, ls=":", color="darkgray")
    ax[1].set_ylim([-0.5, 0.5])
    ax[1].set_xlabel(r"$\nu / Hz$")
    ax[1].semilogx(
        nu,
        deviation,
        marker=".",
        ls="--", 
        color="C1",
        lw=1.5,
        label=r"$1 - \nu F_{\nu, \rm comparison} \, / \,\nu F_{\nu, \rm reference}$",
    )
    ax[1].legend(loc="best")
    fig.savefig(f"{fig_path}")
