import matplotlib.pyplot as plt

class NewFormatter(plt.LogFormatter):
    """
    Subclass Log formatter to pretty print ALL numbers unless they are huge
    """
    def _num_to_string(self, x, vmin, vmax):
        if x > 10000:
            s = '%1.0e' % x
        else:
            s = self._pprint_val(x, vmax - vmin)
        return s

def finalize_plot(ax, log=False, margins=False, **kwargs):
    """
    helper function to finalize a plot
    """
    if kwargs:
        ax.set(**kwargs)
    if log:
        # Formatter instance to use for this ax only
        formatter_x = NewFormatter(labelOnlyBase=False, minor_thresholds=(0.8, 0.5))
        ax.xaxis.set_major_formatter(formatter_x)
        ax.xaxis.set_minor_formatter(formatter_x)
    if not margins:
        ax.margins(x=0)
    #if title is not None:
    #    ax.set_title(title)
    

# def hist(df, prop):

#     labels_x = []
#     labels_y = []
#     hist_data = {'Labels':[], prop:[]}

#     for row in df.itertuples():
#         if not np.isnan(row.flux_x):
#             hist_data['Labels'].append('H$_2$O')
#             hist_data[prop].append(row.Mstar)

#         if not np.isnan(row.flux_y):
#             hist_data['Labels'].append('Neon[II]')
#             hist_data[prop].append(row.Mstar)

#         if np.isnan(row.flux_x) and np.isnan(row.flux_y):
#             hist_data['Labels'].append('Missing')
#             hist_data[prop].append(row.Mstar)



#     hist_data = pd.DataFrame(data=hist_data)