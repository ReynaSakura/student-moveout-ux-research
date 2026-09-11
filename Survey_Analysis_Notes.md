# Survey Analysis Notes

## 0. Analysis Dataset

### Purpose

The survey analysis focuses on respondents who had both:

* previously moved out; and
* unwanted but still usable household items during the move-out process.

### Eligibility Criteria

```python
analysis_df = df[
    (df["has_moved_out"] == "Yes") &
    (df["had_usable_unwanted_items"] == "Yes")
].copy()
```

### Final Sample

* Valid respondents: **N = 39**
* `other_feedback` was excluded from the structured RQ1–RQ3 analysis because it was an open-ended additional feedback field.

### Data Processing

* Single-choice questions were analysed using frequency counts.
* Multiple-choice questions were split into individual response options before counting.
* Percentages were calculated using the eligible sample size (**N = 39**).
* Because multiple-choice questions allow multiple selections, percentages for these questions may sum to more than 100%.

Helper function used for multiple-choice questions:

```python
def count_multiple_choice(df, column):
    return (
        df[column]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
    )
```

---

# RQ1 — Current Behaviour and Awareness

> **Research Question:**
> How do university students currently deal with unwanted but still usable household items when moving out, and how aware are they of available reuse and redistribution channels and potential recipients?

## Analysis Procedure

The cleaned survey dataset was loaded from `cleaned_survey.csv`.

* **Number of respondents:** 39
* **Number of variables:** 26
* All 39 respondents included in this analysis had:

  * moved out before, and
  * had unwanted but still usable household items.

The analysis focused on four aspects of RQ1:

1. Current disposition methods for unwanted usable items
2. Students' first-choice clearing option
3. Awareness and use of available redistribution channels
4. Previous experience with redistribution

### Multiple-response questions

Several survey questions allowed respondents to select multiple options. For these questions, responses were split using `", "` and then expanded using `explode()` before calculating frequencies.

For example:

```python
def count_multiple_choice(df, column):
    return (
        df[column]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
    )
```

Percentages were calculated using the full set of 39 eligible respondents as the denominator:

```python
percentage = count / len(df) * 100
```

Therefore, percentages for multiple-response questions do not necessarily sum to 100%.

---

## RQ1.1 Current Disposition of Unwanted Usable Items

### Variable

`item_disposition`

This was a multiple-response question asking how respondents had dealt with unwanted but still usable household items.

### Results

| Disposition method                   | Count | Percentage |
| ------------------------------------ | ----: | ---------: |
| Give them away to friends/housemates |    32 |      82.1% |
| Throw them away                      |    28 |      71.8% |
| Sell them                            |    24 |      61.5% |
| Give them away online                |    13 |      33.3% |
| Leave them for next occupant         |    11 |      28.2% |
| Recycle                              |     7 |      17.9% |
| Donate to charity/op shop            |     6 |      15.4% |
| Sell online                          |     1 |       2.6% |

### Interpretation

Giving items to friends or housemates was the most commonly reported redistribution method, with 32 respondents (82.1%) selecting it. However, disposal was also highly prevalent, with 28 respondents (71.8%) reporting that they had thrown away usable items.

Selling was also common (24 respondents, 61.5%), while online giving was less common (13 respondents, 33.3%). Formal donation and recycling were reported less frequently.

This suggests that students already use several reuse and redistribution pathways, particularly through existing personal networks. However, disposal remains common even among respondents who had usable unwanted items.

**Key implication for RQ1:**
The problem is not simply that students do not redistribute usable items. Rather, redistribution already occurs, but existing options do not consistently prevent usable items from being discarded.

---

## RQ1.2 First Option Considered

### Variable

`first_option`

This was a single-choice question asking what respondents would consider as their first option when clearing unwanted usable items.

### Results

| First option               | Count | Percentage |
| -------------------------- | ----: | ---------: |
| Sell                       |    17 |      43.6% |
| Give to friends/housemates |    13 |      33.3% |
| Leave for next occupant    |     4 |      10.3% |
| Throw away                 |     3 |       7.7% |
| Give away online           |     1 |       2.6% |
| Recycle                    |     1 |       2.6% |

### Interpretation

Selling was the most frequently selected first option (43.6%), followed by giving items to friends or housemates (33.3%). Only 3 respondents (7.7%) selected throwing items away as their first option.

This differs from the reported overall disposition behaviour, where throwing items away was selected by 71.8% of respondents.

The difference suggests that disposal may not always be the initial preference. Instead, students may first consider reuse-oriented options such as selling or giving items away, with disposal potentially occurring later when those options are unsuccessful, inconvenient, or too time-consuming.

**Key implication for RQ1:**
Students may have an initial preference for reuse or redistribution, but there may be barriers preventing these intentions from consistently becoming successful outcomes.

---

## RQ1.3 Awareness of Redistribution Channels

### Variables

The following six awareness variables were analysed:

* `awareness_online_marketplaces`
* `awareness_university_groups`
* `awareness_social_media`
* `awareness_friends_students`
* `awareness_charity`
* `awareness_other`

Each question recorded whether respondents had used, considered, or heard of the relevant channel, or had never heard of it.

All six variables contained responses from all 39 respondents.

### Results

| Channel             |       Used | Considered but didn't | Heard only | Never heard |
| ------------------- | ---------: | --------------------: | ---------: | ----------: |
| Friends/students    | 23 (59.0%) |            12 (30.8%) |   3 (7.7%) |    1 (2.6%) |
| Social media        | 20 (51.3%) |            10 (25.6%) |  8 (20.5%) |    1 (2.6%) |
| University groups   | 13 (33.3%) |             8 (20.5%) | 10 (25.6%) |   8 (20.5%) |
| Online marketplaces |  8 (20.5%) |            14 (35.9%) | 13 (33.3%) |   4 (10.3%) |
| Charity             |   2 (5.1%) |             9 (23.1%) | 18 (46.2%) |  10 (25.6%) |
| Other               |   1 (2.6%) |              3 (7.7%) |  9 (23.1%) |  26 (66.7%) |

### Interpretation

The most familiar and frequently used redistribution channels were personal networks and social media.

* Friends/students had the highest usage, with 23 respondents (59.0%) reporting that they had used this channel.
* Social media was used by 20 respondents (51.3%).
* University groups were used by 13 respondents (33.3%).
* Online marketplaces were used by 8 respondents (20.5%), although 14 respondents (35.9%) had considered using them but did not.
* Charity channels showed lower levels of use, with only 2 respondents (5.1%) reporting use.
* The "Other" category had very limited awareness, with 26 respondents (66.7%) reporting that they had never heard of such channels.

Overall, the results indicate that students are generally aware of several common redistribution pathways, particularly those embedded in their existing social networks. Therefore, lack of awareness alone does not appear to fully explain why usable items are discarded.

However, awareness does not necessarily translate into successful redistribution. For example, online marketplaces had relatively high proportions of respondents who had considered but not used them, suggesting that barriers may exist after awareness.

**Key implication for RQ1:**
The design opportunity should not focus solely on increasing awareness of redistribution channels. It should also reduce the effort and uncertainty involved in actually using these channels.

---

## RQ1.4 Previous Redistribution Experience

### Variable

`tried_redistribution`

### Results

| Tried redistribution | Count | Percentage |
| -------------------- | ----: | ---------: |
| Yes                  |    36 |      92.3% |
| No                   |     3 |       7.7% |

Most respondents (36, 92.3%) had previously tried to redistribute an unwanted usable item.

Only three respondents (7.7%) reported that they had not tried redistribution.

### Supporting observation

The three respondents who had not tried redistribution showed mixed levels of awareness across different channels. Because this subgroup contains only three respondents, these responses are treated as supporting observations rather than a basis for generalisation.

### Interpretation

The high proportion of respondents who had already attempted redistribution provides further evidence that the issue is not primarily a lack of willingness to reuse items.

Instead, the survey population appears to have substantial prior experience with redistribution. This makes the barriers encountered during redistribution particularly relevant to understanding why disposal still occurs.

The results from this question should therefore be considered together with the barrier analysis in **RQ2**, which examines the effort, uncertainty, coordination, logistical, and interpersonal factors associated with redistribution and disposal.

---

# RQ1 Overall Finding

## Finding 1: Redistribution is already common, but disposal remains common

The RQ1 analysis shows that students already engage with multiple reuse and redistribution pathways. Giving items to friends or housemates was the most commonly reported method (82.1%), while selling was also common (61.5%). In addition, 92.3% of respondents had previously tried redistribution.

However, disposal was also highly prevalent, with 71.8% of respondents reporting that they had thrown away usable items.

The comparison between first-choice behaviour and reported past behaviour provides an important indication: only 7.7% selected throwing items away as their first option, despite 71.8% reporting that they had done so. This suggests that disposal may often occur after other options have been considered or attempted rather than being the preferred initial choice.

Awareness of redistribution channels was generally present, particularly for friends/students and social media. Therefore, lack of awareness alone does not appear to explain the persistence of disposal.

### RQ1 conclusion

The survey suggests that students are generally willing to consider or attempt reuse and redistribution, but existing pathways do not always translate this willingness into successful redistribution.

This supports investigating **what makes redistribution difficult**, particularly in terms of effort, uncertainty, coordination, and logistical constraints. These issues are examined further in **RQ2**.


---

# RQ2 — Barriers to Redistribution

> **Research Question:**
> What barriers and considerations influence university students' decisions to redistribute or discard unwanted but still usable household items when moving out?

## Analysis Procedure

The cleaned survey dataset was loaded from `cleaned_survey.csv`.

* **Number of respondents:** 39
* **Number of variables:** 26
* The analysis used the same 39 eligible respondents as RQ1.

RQ2 examined five areas:

1. Factors associated with choosing disposal
2. Difficulties experienced when redistributing items
3. Difficulties when handling multiple items
4. Factors considered when deciding how to deal with an item
5. Concerns and discomfort associated with handing items to strangers

Several RQ2 questions were multiple-response questions. For these variables, responses were split using `", "` and expanded using `explode()` before calculating frequencies.

```python id="3k7px1"
counts = (
    df["column_name"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
)
```

Percentages were calculated using the 39 eligible respondents as the denominator.

Because respondents could select multiple options, percentages for these questions do not necessarily sum to 100%.

---

## RQ2.1 Factors Associated with Disposal

### Variable

`discard_factors`

This was a multiple-response question asking about factors that may contribute to throwing away usable household items.

### Results

| Factor                                         | Count | Percentage |
| ---------------------------------------------- | ----: | ---------: |
| Not sure anyone will want it                   |    27 |      69.2% |
| Too much time to find someone                  |    26 |      66.7% |
| Too much effort to arrange                     |    25 |      64.1% |
| Pickup arrangements are inconvenient           |    20 |      51.3% |
| Need to get rid of it quickly                  |    18 |      46.2% |
| Item has little or no monetary value           |    16 |      41.0% |
| Too much messaging or coordination             |    13 |      33.3% |
| Left it too late to arrange anything           |     6 |      15.4% |
| Recipient is too far away                      |     5 |      12.8% |
| Most people I know were also moving out        |     5 |      12.8% |
| Safety or privacy concern                      |     2 |       5.1% |
| Have never thrown away a usable household item |     1 |       2.6% |

### Interpretation

The most commonly selected factors were uncertainty, time, and effort.

The most frequently reported factor was uncertainty about whether anyone would want the item (27 respondents, 69.2%). This was followed by the time required to find someone (26, 66.7%) and the effort required to arrange redistribution (25, 64.1%).

Logistical issues were also common. Pickup arrangements were considered inconvenient by 20 respondents (51.3%), while 18 respondents (46.2%) reported needing to get rid of items quickly.

These results suggest that disposal is associated with several practical barriers rather than a single factor. In particular, students may find redistribution unattractive when they are uncertain about finding a recipient or when the process requires substantial time and effort.

The response "I have never thrown away a usable household item" was selected by one respondent. This is not interpreted as a barrier and is retained only as an individual response.

**Key implication:**
A redistribution system should reduce uncertainty about finding recipients and minimise the time and effort required to complete redistribution.

---

## RQ2.2 Difficulties Experienced During Redistribution

### Variable

`redistribution_difficulties`

This was a multiple-response question asking about difficulties experienced when trying to sell or give away items.

### Results

| Difficulty                             | Count | Percentage |
| -------------------------------------- | ----: | ---------: |
| Setting a price                        |    20 |      51.3% |
| Finding interested people              |    20 |      51.3% |
| Describing the item                    |    12 |      30.8% |
| Transporting the item                  |    11 |      28.2% |
| Arranging pickup                       |    10 |      25.6% |
| Negotiating                            |     8 |      20.5% |
| Taking photos / creating a listing     |     8 |      20.5% |
| People cancelling / not showing up     |     6 |      15.4% |
| Responding to messages                 |     5 |      12.8% |
| Have not tried to sell/give away items |     3 |       7.7% |

### Interpretation

The two most frequently reported difficulties were setting a price and finding interested people, both selected by 20 respondents (51.3%).

Other difficulties were related to preparing and completing a redistribution transaction, including describing the item (30.8%), transporting the item (28.2%), and arranging pickup (25.6%).

Less frequently reported difficulties included negotiating, creating listings, dealing with cancellations or no-shows, and responding to messages.

Overall, the results indicate that redistribution involves friction across multiple stages of the process, from preparing an item for redistribution to finding a recipient and completing the handover.

**Key implication:**
Reducing the amount of work required to create and coordinate a redistribution transaction may make reuse more practical, particularly for low-value household items.

---

## RQ2.3 Difficulties When Redistributing Multiple Items

### Variable

`multiple_item_difficulties`

This was a multiple-response question examining difficulties that arise when students need to redistribute several items at the same time.

### Results

| Difficulty                                           | Count | Percentage |
| ---------------------------------------------------- | ----: | ---------: |
| Messaging different people                           |    19 |      48.7% |
| Arranging multiple pickups                           |    17 |      43.6% |
| Finding recipients for all items before the deadline |    17 |      43.6% |
| Keeping track of who wanted which item               |    16 |      41.0% |
| Writing descriptions or setting prices               |    15 |      38.5% |
| Taking photos of multiple items                      |    10 |      25.6% |
| Creating separate listings                           |    10 |      25.6% |
| It was not difficult                                 |     1 |       2.6% |

### Interpretation

Managing multiple items introduces additional coordination work.

The most frequently reported difficulty was messaging different people (48.7%). This was followed by arranging multiple pickups and finding recipients for all items before the deadline (both 43.6%).

Tracking which person wanted which item was also frequently reported (41.0%).

These results suggest that the difficulty of redistribution can increase when students have multiple items to clear. Instead of dealing with a single transaction, students may need to manage several recipients, conversations, listings, and pickup arrangements simultaneously.

**Key implication:**
A system should support multiple items and recipients within a coordinated workflow rather than treating each item as an entirely separate transaction.

---

## RQ2.4 Factors Considered When Deciding What to Do With an Item

### Variable

`decision_factors`

This was a multiple-response question examining the factors respondents considered when deciding how to deal with an unwanted usable item.

### Results

| Decision factor                               | Count | Percentage |
| --------------------------------------------- | ----: | ---------: |
| How quickly I need to get rid of it           |    22 |      56.4% |
| Amount of effort required                     |    19 |      48.7% |
| Likelihood of finding someone who wants it    |    19 |      48.7% |
| Convenience                                   |    17 |      43.6% |
| Item's monetary value                         |    16 |      41.0% |
| Distance / pickup difficulty                  |     8 |      20.5% |
| Availability of transport                     |     5 |      12.8% |
| Feeling responsible for wasting a usable item |     3 |       7.7% |
| Privacy or safety concerns                    |     1 |       2.6% |

### Interpretation

The most commonly selected decision factor was how quickly the respondent needed to get rid of the item (56.4%).

Effort and likelihood of finding someone were each selected by 48.7% of respondents, followed by convenience (43.6%) and monetary value (41.0%).

This indicates that students' decisions are influenced strongly by the practical trade-off between the value of redistribution and the effort, time, and uncertainty involved.

The relatively low frequency of privacy or safety concerns as a general decision factor (2.6%) suggests that these concerns may not be a primary consideration for most respondents when deciding what to do with an item. However, the separate stranger-related questions show that specific handover situations can still create discomfort.

**Key implication:**
The system should make redistribution sufficiently quick and convenient to compete with disposal, particularly when the item has low monetary value.

---

## RQ2.5 Concern About Giving Items to Strangers

### Variable

`stranger_concern`

Respondents rated their level of concern about giving unwanted items to people they did not know.

### Results

| Concern level | Count | Percentage |
| ------------- | ----: | ---------: |
| 1             |     4 |      10.3% |
| 2             |     6 |      15.4% |
| 3             |    12 |      30.8% |
| 4             |    14 |      35.9% |
| 5             |     3 |       7.7% |

Combining ratings 4 and 5:

* **High concern (4–5): 17 respondents (43.6%)**
* Neutral (3): 12 respondents (30.8%)
* Lower concern (1–2): 10 respondents (25.6%)

### Interpretation

Although privacy and safety were not frequently selected as a general decision factor, 17 respondents (43.6%) gave a concern rating of 4 or 5 when specifically asked about giving items to strangers.

This suggests that stranger-related concerns may become more relevant when the redistribution process involves direct interaction with unfamiliar recipients.

Therefore, privacy and safety should not necessarily be treated as the primary barrier to redistribution, but they remain relevant when designing the handover process.

---

## RQ2.6 Specific Discomforts When Dealing With Strangers

### Variable

`stranger_discomfort`

This was a multiple-response question asking what aspects of interacting with strangers would make respondents uncomfortable.

### Results

| Source of discomfort                             | Count | Percentage |
| ------------------------------------------------ | ----: | ---------: |
| Sharing phone number or personal contact details |    26 |      66.7% |
| Sharing home address                             |    25 |      64.1% |
| Meeting in a private or unfamiliar location      |    25 |      64.1% |
| Meeting someone they do not know                 |    17 |      43.6% |
| Would not feel uncomfortable                     |     4 |      10.3% |

### Interpretation

The most common concerns were related to sharing personal information and arranging physical handovers.

Sharing a phone number or personal contact details was selected by 26 respondents (66.7%). Sharing a home address and meeting in a private or unfamiliar location were each selected by 25 respondents (64.1%).

Meeting someone they did not know was also a concern for 17 respondents (43.6%).

These findings provide more specific evidence about the nature of stranger-related concerns. Rather than simply being about interacting with strangers, discomfort is particularly associated with exposing personal contact information, home addresses, and potentially unfamiliar meeting locations.

**Key implication:**
If redistribution involves strangers, the system should minimise unnecessary exposure of personal contact information and support safer, clearly defined handover arrangements.

---

# RQ2 Overall Finding

## Finding 2: Redistribution is constrained by effort, uncertainty, and coordination

The RQ2 analysis identifies three closely related sources of friction in redistribution.

### 1. Uncertainty about finding recipients

The most frequently reported disposal factor was uncertainty about whether anyone would want the item (69.2%). Finding interested people was also one of the most common difficulties when attempting redistribution (51.3%).

This suggests that students may be reluctant to invest effort in redistribution when the outcome is uncertain.

### 2. Time and effort required

Time pressure and effort were consistently important across the results.

* 66.7% reported that finding someone takes too much time.
* 64.1% reported that arranging redistribution takes too much effort.
* 56.4% considered how quickly they needed to get rid of the item when making decisions.
* 51.3% reported pickup arrangements as inconvenient.

These results indicate that redistribution competes with disposal partly on convenience and speed.

### 3. Coordination becomes harder with multiple items

When dealing with multiple items, messaging different people (48.7%), arranging multiple pickups (43.6%), finding recipients for all items before the deadline (43.6%), and tracking who wanted which item (41.0%) were common difficulties.

This indicates that coordination overhead can increase substantially when several items need to be redistributed at the same time.

### 4. Privacy and safety during stranger handovers

General privacy or safety concerns were selected relatively infrequently as a disposal or decision factor. However, more specific stranger-related questions revealed substantial discomfort around sharing phone numbers, home addresses, and meeting in unfamiliar locations.

Therefore, privacy and safety appear to be a **secondary but important design consideration**, particularly for systems that facilitate redistribution between people who do not already know each other.

---

## RQ2 Conclusion

Overall, the survey suggests that students face a combination of **uncertainty, time pressure, effort, and coordination costs** when redistributing unwanted usable household items.

The findings indicate that improving redistribution is not simply a matter of providing another place to list items. A useful system would need to reduce the work involved in finding recipients, managing multiple items, coordinating pickups, and completing transactions within the available time.

These findings also provide a basis for RQ3, which examines how **move-out deadline pressure changes redistribution decisions and the relative importance of these barriers**.

---

# RQ3 — Effect of Move-out Time Pressure

> **Research Question:**
> How does move-out time pressure affect students' redistribution decisions and the importance of the barriers they experience?

## Analysis Procedure

The cleaned survey dataset was loaded from `cleaned_survey.csv`.

* **Number of respondents:** 39
* **Number of variables:** 26
* The analysis used the same 39 eligible respondents as RQ1 and RQ2.

RQ3 examined how students' intended actions change depending on the amount of time remaining before move-out.

Four variables were analysed:

1. Intended action when approximately three weeks remain
2. Intended action when only one to two days remain
3. Concern about completing redistribution before the move-out deadline
4. Amount of time respondents are willing to spend redistributing an item

The three-week and one-to-two-day responses were compared directly to identify changes in intended behaviour as the deadline approaches.

---

## RQ3.1 Intended Action Three Weeks Before Move-out

### Variable

`action_three_weeks`

This was a single-choice question asking what respondents would do with an unwanted usable item when they still had approximately three weeks before moving out.

### Results

| Intended action                | Count | Percentage |
| ------------------------------ | ----: | ---------: |
| Sell it                        |    20 |      51.3% |
| Give it to a friend/housemate  |     9 |      23.1% |
| Give it away                   |     6 |      15.4% |
| Throw it away                  |     2 |       5.1% |
| Recycle it                     |     1 |       2.6% |
| Leave it for the next occupant |     1 |       2.6% |

### Interpretation

When respondents had approximately three weeks remaining, selling was the most common intended action, selected by 20 respondents (51.3%).

Giving items to friends or housemates was the second most common option (23.1%), followed by giving items away (15.4%).

Only 2 respondents (5.1%) selected throwing the item away at this stage.

This suggests that when more time is available, respondents are more likely to consider redistribution methods that may require additional time or coordination, particularly selling.

---

## RQ3.2 Intended Action One to Two Days Before Move-out

### Variable

`action_one_two_days`

This was a single-choice question asking what respondents would do with an unwanted usable item when only one to two days remained before moving out.

### Results

| Intended action                | Count | Percentage |
| ------------------------------ | ----: | ---------: |
| Throw it away                  |    14 |      35.9% |
| Give it away                   |     9 |      23.1% |
| Give it to a friend/housemate  |     6 |      15.4% |
| Leave it for the next occupant |     5 |      12.8% |
| Recycle it                     |     3 |       7.7% |
| Sell it                        |     1 |       2.6% |
| Donate it                      |     1 |       2.6% |

### Interpretation

When only one to two days remained, throwing the item away became the most common intended action, selected by 14 respondents (35.9%).

Giving the item away remained relatively common (23.1%), while giving it to a friend or housemate was selected by 15.4%.

In contrast, selling dropped substantially, with only one respondent (2.6%) selecting it.

This suggests that when little time remains, respondents appear to favour options that can be completed more quickly or with less coordination.

---

## RQ3.3 Comparison Across Different Time Points

The two scenarios were compared to examine how intended behaviour changes as the move-out deadline approaches.

| Intended action     | 3 weeks before | 1–2 days before |
| ------------------- | -------------: | --------------: |
| Sell                |          51.3% |            2.6% |
| Give away           |          15.4% |           23.1% |
| Friend/housemate    |          23.1% |           15.4% |
| Throw away          |           5.1% |           35.9% |
| Recycle             |           2.6% |            7.7% |
| Leave next occupant |           2.6% |           12.8% |
| Donate              |             0% |            2.6% |

### Interpretation

The comparison shows a substantial change in intended behaviour as the deadline approaches.

The most notable change is selling:

* **Three weeks before:** 51.3%
* **One to two days before:** 2.6%

At the same time, throwing the item away increases:

* **Three weeks before:** 5.1%
* **One to two days before:** 35.9%

Giving items away also becomes somewhat more common, increasing from 15.4% to 23.1%.

Overall, the results suggest that respondents shift away from options that may require more time or coordination and towards faster or more immediately executable options as the deadline approaches.

This should be interpreted as a pattern in **intended behaviour between two hypothetical time points**, rather than evidence of a causal effect of the deadline.

**Key implication:**
A redistribution system should be designed to remain practical even when users have very limited time remaining before move-out.

---

## RQ3.4 Concern About Completing Redistribution Before the Deadline

### Variable

`deadline_concern`

Respondents rated their level of concern about being able to complete redistribution before the move-out deadline.

### Results

| Concern level | Count | Percentage |
| ------------- | ----: | ---------: |
| 1             |     4 |      10.3% |
| 2             |    11 |      28.2% |
| 3             |    10 |      25.6% |
| 4             |    11 |      28.2% |
| 5             |     3 |       7.7% |

Combining the responses:

* **High concern (4–5): 14 respondents (35.9%)**
* **Neutral (3): 10 respondents (25.6%)**
* **Lower concern (1–2): 15 respondents (38.5%)**

### Interpretation

Concern about completing redistribution before the deadline was relatively mixed.

While 35.9% of respondents selected a high concern rating (4–5), 38.5% selected a lower concern rating (1–2), and 25.6% selected the neutral rating.

Therefore, the results do **not** indicate that most respondents experience a high level of subjective concern about the deadline.

However, the behavioural comparison between three weeks and one to two days shows a substantial shift in intended actions as available time decreases.

This suggests an important distinction: **students do not necessarily report feeling highly concerned about the deadline, but reduced available time may still influence which disposal or redistribution options appear practical.**

---

## RQ3.5 Willingness to Spend Time on Redistribution

### Variable

`willing_time`

This question measured how much time respondents would be willing to spend redistributing an unwanted item.

### Results

| Time willing to spend  | Count | Percentage |
| ---------------------- | ----: | ---------: |
| Less than 10 minutes   |    14 |      35.9% |
| 10–30 minutes          |    14 |      35.9% |
| It depends on the item |     6 |      15.4% |
| 30–60 minutes          |     4 |      10.3% |
| More than 60 minutes   |     1 |       2.6% |

Combining the fixed time categories:

* **30 minutes or less:** 28 respondents (71.8%)
* **More than 30 minutes:** 5 respondents (12.8%)
* **Depends on the item:** 6 respondents (15.4%)

### Interpretation

Most respondents indicated a relatively low tolerance for the time required to redistribute an item.

Fourteen respondents (35.9%) were willing to spend less than 10 minutes, while another 14 (35.9%) were willing to spend 10–30 minutes.

Overall, 71.8% selected a fixed time commitment of 30 minutes or less.

Only 5 respondents (12.8%) selected more than 30 minutes, while 15.4% indicated that their willingness depended on the item.

This suggests that a redistribution process requiring substantial time may be difficult to sustain, particularly for low-value items or when the move-out deadline is close.

**Key implication:**
The core redistribution process should minimise the amount of active time required from the user.

---

# RQ3 Overall Finding

## Finding 3: Increasing deadline pressure shifts behaviour towards faster and lower-coordination options

The RQ3 analysis indicates that available time is associated with substantial differences in students' intended clearing behaviour.

When approximately three weeks remained, selling was the most common intended action (51.3%), while only 5.1% selected throwing the item away.

When only one to two days remained, selling dropped to 2.6%, while throwing the item away increased to 35.9%.

At the same time, 71.8% of respondents indicated that they would be willing to spend 30 minutes or less on redistribution.

These findings suggest that students may be willing to redistribute items when sufficient time is available, but options requiring more time or coordination become less attractive as the deadline approaches.

Importantly, subjective deadline concern was mixed: 35.9% reported high concern, while 38.5% reported low concern. Therefore, the findings should not be interpreted as showing that most students feel anxious about the deadline.

Instead, the stronger evidence comes from the **change in intended behaviour between the two time scenarios**.

### RQ3 conclusion

Move-out time pressure appears to affect the practicality of different redistribution options. As available time decreases, students appear more likely to choose faster or lower-coordination options, including disposal.

The results therefore support designing redistribution around **speed, low effort, and minimal coordination**, particularly for users approaching their move-out deadline.

This finding should be considered together with RQ2, which identified uncertainty, effort, and coordination as major barriers to redistribution.


---

# Cross-RQ Findings / User Needs

The findings from RQ1–RQ3 were synthesised to identify recurring patterns across students' current behaviour, redistribution barriers, and responses to move-out time pressure.

Rather than treating each research question independently, the analysis considered how the findings collectively explain why students may dispose of usable items even when they are willing to redistribute them.

---

## 5.1 Finding 1 — Students are willing to redistribute, but redistribution does not consistently prevent disposal

### Evidence from RQ1

Redistribution was already common among respondents:

* 82.1% had given unwanted usable items to friends or housemates.
* 61.5% had sold items.
* 33.3% had given items away online.
* 92.3% had previously tried to redistribute an item.

However, disposal was also common, with 71.8% reporting that they had thrown away usable household items.

The first-choice results provide additional context. Only 7.7% selected throwing an item away as their first option, compared with 43.6% selecting selling and 33.3% selecting giving the item to friends or housemates.

### Interpretation

These results suggest that disposal is not necessarily the preferred starting point. Students appear willing to consider or attempt reuse and redistribution, but redistribution does not always result in a successful or practical outcome.

Therefore, the design problem is not simply encouraging students to redistribute. It is about making redistribution sufficiently practical that an existing willingness to reuse can be converted into a successful outcome.

### User Need

> **Students need a redistribution process that makes it practical to successfully pass on usable items rather than defaulting to disposal.**

---

## 5.2 Finding 2 — Students need easier ways to find suitable recipients

### Evidence from RQ1 and RQ2

Awareness of existing channels was generally present, particularly for personal networks and social media:

* 59.0% had used friends/students as a channel.
* 51.3% had used social media.
* 33.3% had used university groups.
* 20.5% had used online marketplaces.

However, awareness did not necessarily translate into successful redistribution.

In RQ2:

* 69.2% reported being unsure whether anyone would want the item when considering disposal.
* 66.7% reported that finding someone takes too much time.
* 51.3% reported difficulty finding interested people during redistribution.

### Interpretation

The results indicate that simply knowing that redistribution channels exist may not be sufficient. Students may still be uncertain about whether a suitable recipient can be found and may have to spend considerable time searching for one.

This suggests a gap between **awareness of channels** and **confidence that a suitable recipient will actually be found**.

### User Need

> **Students need an easy way to discover suitable recipients for their unwanted items, with greater confidence that someone is interested.**

---

## 5.3 Finding 3 — The redistribution process needs to require less time and effort

### Evidence from RQ2 and RQ3

Time and effort were repeatedly identified as important considerations.

In RQ2:

* 66.7% reported that finding someone takes too much time.
* 64.1% reported that redistribution takes too much effort to arrange.
* 51.3% reported that pickup arrangements are inconvenient.
* 56.4% considered how quickly they needed to get rid of an item when making decisions.

The willingness-to-spend-time results in RQ3 further support this pattern:

* 35.9% were willing to spend less than 10 minutes.
* 35.9% were willing to spend 10–30 minutes.
* Overall, 71.8% selected 30 minutes or less.

### Interpretation

Students generally appear to have a limited tolerance for the time required to redistribute an item.

This is particularly important for household items with relatively low monetary value. If redistribution requires substantial effort, students may perceive disposal as a more convenient alternative.

### User Need

> **Students need a redistribution process that can be completed with minimal time and effort.**

---

## 5.4 Finding 4 — Managing multiple items creates additional coordination problems

### Evidence from RQ2

When respondents considered redistributing multiple items, the most common difficulties were:

* Messaging different people: 48.7%
* Arranging multiple pickups: 43.6%
* Finding recipients for all items before the deadline: 43.6%
* Keeping track of who wanted which item: 41.0%
* Writing descriptions or setting prices: 38.5%

These difficulties indicate that the burden of redistribution can increase when students need to clear several items simultaneously.

### Interpretation

Existing redistribution processes may require students to manage separate listings, conversations, recipients, and pickup arrangements.

For students moving out, this creates additional coordination work at a time when they may already be managing multiple tasks.

### User Need

> **Students need a way to manage multiple items, recipients, and handover arrangements without having to coordinate each item separately.**

---

## 5.5 Finding 5 — Redistribution needs to remain effective under time pressure

### Evidence from RQ3

Students' intended actions changed substantially between the two time scenarios.

When approximately three weeks remained:

* 51.3% intended to sell the item.
* 23.1% intended to give it to a friend/housemate.
* 15.4% intended to give it away.
* 5.1% intended to throw it away.

When only one to two days remained:

* 35.9% intended to throw the item away.
* 23.1% intended to give it away.
* 15.4% intended to give it to a friend/housemate.
* 2.6% intended to sell it.

Selling therefore decreased from 51.3% to 2.6%, while throwing the item away increased from 5.1% to 35.9%.

### Interpretation

The comparison suggests that as the available time decreases, options requiring more time or coordination become less practical, while faster options become more attractive.

The results do not establish that deadline pressure directly causes disposal. However, the difference between the two scenarios indicates that the amount of time available is an important consideration when choosing how to clear an item.

### User Need

> **Students need redistribution options that can remain practical and achievable even when only a short amount of time remains before move-out.**

---

## 5.6 Finding 6 — Stranger-based redistribution should minimise privacy and safety concerns

### Evidence from RQ2

General privacy or safety concerns were not among the most frequently selected decision factors. Only 1 respondent (2.6%) selected privacy or safety concerns as a decision factor.

However, when respondents were asked specifically about interacting with strangers, more substantial concerns were reported:

* 66.7% were uncomfortable sharing their phone number or personal contact details.
* 64.1% were uncomfortable sharing their home address.
* 64.1% were uncomfortable meeting in a private or unfamiliar location.
* 43.6% were uncomfortable meeting someone they did not know.

### Interpretation

The results suggest that privacy and safety are not necessarily the primary reason students choose disposal. However, they can become important when redistribution requires direct interaction with unfamiliar recipients.

Therefore, privacy and safety should be treated as a supporting design consideration rather than the central explanation for disposal behaviour.

### User Need

> **Students need redistribution and handover arrangements that minimise unnecessary sharing of personal information and support safer interactions with unfamiliar recipients.**

---

# Synthesised User Needs

Across RQ1–RQ3, the survey findings identify six recurring user needs:

| Priority area           | Evidence from survey                                                                                                   | Synthesised user need                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Recipient discovery     | 69.2% unsure anyone will want the item; 51.3% difficulty finding interested people                                     | Students need an easy way to find suitable recipients.                                   |
| Low effort and time     | 66.7% reported finding someone takes too much time; 64.1% reported too much effort; 71.8% willing to spend ≤30 minutes | Students need a quick and low-effort redistribution process.                             |
| Coordination            | 48.7% messaging different people; 43.6% multiple pickups                                                               | Students need to coordinate redistribution without managing many separate interactions.  |
| Multiple items          | 43.6% difficulty finding recipients for all items; 41.0% difficulty tracking who wanted which item                     | Students need to manage multiple items and recipients together.                          |
| Deadline responsiveness | Selling decreased from 51.3% to 2.6%; disposal increased from 5.1% to 35.9%                                            | Students need redistribution that remains practical close to the move-out deadline.      |
| Privacy and safety      | 66.7% uncomfortable sharing contact details; 64.1% uncomfortable sharing home address                                  | Students need safer handover arrangements with limited exposure of personal information. |

---

# Overall Synthesis

Taken together, the survey findings suggest that the central challenge is not a lack of awareness or willingness to redistribute.

Students already use redistribution channels, and most respondents (92.3%) had previously tried to redistribute unwanted items. However, redistribution can become impractical when students are uncertain whether a recipient will be found, when the process requires too much time or effort, or when multiple items require separate coordination.

The effect of available time is particularly important. The comparison between three weeks and one to two days before move-out suggests that students shift towards faster and lower-coordination options as the deadline approaches, including disposal.

Therefore, the survey findings point towards a design direction centred on:

1. **Reducing uncertainty** about whether an item will find a recipient.
2. **Reducing user effort and time** required to redistribute an item.
3. **Simplifying coordination** between items, recipients, and pickups.
4. **Supporting multiple items** within a single workflow.
5. **Maintaining practicality under time pressure** close to move-out.
6. **Supporting safer and more privacy-conscious handovers** when recipients are unfamiliar.

These user needs provide the evidence base for translating the survey findings into system and functional requirements in the subsequent requirements analysis.

