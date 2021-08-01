# Use Of Force Examples

## Properties

| property name | data type |
| --- | --- |
| force_applied | string |
| deadly_force | string |

### Force Applied

The `force_applied` property refers to actions taken by law enforcement as described by the [Use of Force Continuum](https://nij.ojp.gov/topics/articles/use-force-continuum) as described by the U.S. Department of Justice. Information systems creators may wish to store the human-readable descriptions of uses of force in their systems as metadata. For convience, I've provided the human-readable names and descriptions along side of the slugs used in the schema. You can find examples of each levle of force on the [U.S. National Institute of Justice's website](https://nij.ojp.gov/topics/articles/use-force-continuum).

| Level of Force | slug | description |
| --- | --- | --- |
| Officer Presence | officer-presence | No force is used. Considered the best way to resolve a situation. |
| Verbalization | verbalization | Force is not-physical. |
| Empty-Hand Control | empty-hand-control | Officers use bodily force to gain control of a situation. |
| Less-Lethal Methods | less-lethal | Officers use less-lethal technologies to gain control of a situation. |
| Lethal Force | lethal | Officers use lethal weapons to gain control of a situation. Should only be used if a suspect poses a serious threat to the officer or another individual. |

### Deadly Force

The `deadly_force` property allows creators and users of information systems to distinguish between different types of deadly force. Possible values for this property originates from [Scott Harman-Heath's Renaming Deadly Force paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3660954).

| Deadly Force | slug |
| --- | --- |
| Anticipatory | anticipatory  |
| Preemptive | preemptive |
| Reactive | reactive |
