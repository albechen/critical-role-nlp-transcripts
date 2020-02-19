import seaborn as sns
import matplotlib.pyplot as plt

from .e_agg_df_count import group_by_person_episode, count_per_episode


def lineplot_per_ep (org_names, matt_nomatt, C1_C2):
    person_episode_group = group_by_person_episode(org_names)
    if matt_nomatt == 'nomatt':
        person_episode_group = person_episode_group.loc[person_episode_group['person'] != 'matt']

    sns.set_style('whitegrid')

    plt.figure(figsize=(25,5))
    ax = sns.lineplot(x="episode", y="time_count", 
        data=person_episode_group, hue='person', marker='o')
    if C1_C2 == 'C1':
        ax.set(xlim=(1, 115))
    else:
        ax.set(xlim=(1, 90))
    ax.legend(bbox_to_anchor=(1, 1))
    ax

def lineplot_cont_count (org_names, matt_nomatt, C1_C2):
    person_episode_group = group_by_person_episode(org_names)
    count_per_ep = count_per_episode(person_episode_group)
    if matt_nomatt == 'nomatt':
        count_per_ep = count_per_ep.loc[count_per_ep['person'] != 'matt']

    sns.set_style('whitegrid')

    plt.figure(figsize=(7,5))
    ax = sns.lineplot(x="episode", y="cont_time_count", 
        data=count_per_ep, hue='person')

    if C1_C2 == 'C1':
        ax.set(xlim=(1, 115))
    else:
        ax.set(xlim=(1, 90))

    ax.legend(bbox_to_anchor=(1, 1))
    ax

def densityplot_time_per_ep (org_name):
    C1_person_episode_group = group_by_person_episode(org_name)
    names = ['laura', 'matt', 
            'marisha', 'sam', 'taliesin', 
            'liam', 'travis', 'ashley', 
            ]
            #'orion', 'guest'
    plt.figure(figsize=(7,5))
    for name in names:
        g = sns.kdeplot(C1_person_episode_group["time_count"][(C1_person_episode_group["person"] == name)], shade=True)
    g.legend(names)
    g.set_xlim(left=0)