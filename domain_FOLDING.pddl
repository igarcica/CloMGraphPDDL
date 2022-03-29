(define (domain FOLDING)
	(:requirements :strips)
	(:predicates (PP2) (PP2-Pie) (Pie) (L-PP-Pie) (PP-Pie) (PP) 
			(LC-RC) (FL-FR) (I) (FR-R2) (FR-RC) (RE-RC) (RC) 
			(Crumpled) (Flat) (sFolded) (Folded) )

	(:action GoToCenter-B
		:precondition (and (PP2) (LC-RC) (Crumpled))
		:effect (and (Flat) (not (Crumpled)) ))

	(:action PlaceFlatOnTable-A
		:precondition (and (PP2) (LC-RC) (Flat))
		:effect (and (PP2-Pie) (not (PP2)) (FL-FR) (not (LC-RC)) ))

	(:action ReleaseFlatOnTable
		:precondition (and (PP2-Pie) (FL-FR) (Flat))
		:effect (and (Pie) (not (PP2-Pie)) (I) (not (FL-FR)) ))

	(:action FoldOnTable-A
		:precondition (and (PP2-Pie) (FL-FR) (Flat))
		:effect (and (Pie) (not (PP2-Pie)) (I) (not (FL-FR)) (sFolded) (not (Flat)) ))

	(:action FoldOnTable-B
		:precondition (and (PP2-Pie) (FL-FR) (sFolded))
		:effect (and (Pie) (not (PP2-Pie)) (I) (not (FL-FR)) (Folded) (not (sFolded)) ))

	(:action TraceEdge-A
		:precondition (and (PP2-Pie) (FR-R2) (sFolded))
		:effect (and (FR-RC) (not (FR-R2)) ))

	(:action FoldOnTable-C
		:precondition (and (PP2-Pie) (FR-RC) (sFolded))
		:effect (and (Pie) (not (PP2-Pie)) (I) (not (FR-RC)) ))

	(:action GoToCenter-A
		:precondition (and (PP2-Pie) (LC-RC) (Crumpled))
		:effect (and (PP2) (not (PP2-Pie)) (Flat) (not (Crumpled)) ))

	(:action FoldOnTable-D
		:precondition (and (PP2-Pie) (LC-RC) (Flat))
		:effect (and (Pie) (not (PP2-Pie)) (I) (not (LC-RC)) (sFolded) (not (Flat)) ))

	(:action FoldOnTable-E
		:precondition (and (PP2-Pie) (LC-RC) (sFolded))
		:effect (and (Pie) (not (PP2-Pie)) (I) (not (LC-RC)) (Folded) (not (sFolded)) ))

	(:action TraceEdge-B
		:precondition (and (PP2-Pie) (RE-RC) (Crumpled))
		:effect (and (LC-RC) (not (RE-RC)) ))

	(:action TraceEdge-C
		:precondition (and (L-PP-Pie) (RE-RC) (Crumpled))
		:effect (and (PP2-Pie) (not (L-PP-Pie)) (LC-RC) (not (RE-RC)) ))

	(:action Grasp-A
		:precondition (and (Pie) (I) (Crumpled))
		:effect (and (PP-Pie) (not (Pie)) (RC) (not (I)) ))

	(:action Grasp-B
		:precondition (and (Pie) (I) (Flat))
		:effect (and (PP2-Pie) (not (Pie)) (LC-RC) (not (I)) ))

	(:action Grasp-C
		:precondition (and (Pie) (I) (sFolded))
		:effect (and (PP2-Pie) (not (Pie)) (FL-FR) (not (I)) ))

	(:action Grasp-D
		:precondition (and (Pie) (I) (sFolded))
		:effect (and (PP2-Pie) (not (Pie)) (FR-RC) (not (I)) ))

	(:action Grasp-E
		:precondition (and (Pie) (I) (sFolded))
		:effect (and (PP2-Pie) (not (Pie)) (LC-RC) (not (I)) ))

	(:action Grasp-F
		:precondition (and (Pie) (I) (sFolded))
		:effect (and (PP-Pie) (not (Pie)) (RC) (not (I)) ))

	(:action HoldToRegrasp
		:precondition (and (PP) (RC) (Crumpled))
		:effect (and (PP2) (not (PP)) (LC-RC) (not (RC)) ))

	(:action Lift-A
		:precondition (and (PP-Pie) (RC) (Crumpled))
		:effect (and (PP2-Pie) (not (PP-Pie)) (RE-RC) (not (RC)) ))

	(:action Lift-C
		:precondition (and (PP-Pie) (RC) (Crumpled))
		:effect (and (L-PP-Pie) (not (PP-Pie)) (RE-RC) (not (RC)) ))

	(:action RemoveTableContact
		:precondition (and (PP-Pie) (RC) (Crumpled))
		:effect (and (PP) (not (PP-Pie)) ))

	(:action Lift-D
		:precondition (and (PP-Pie) (RC) (sFolded))
		:effect (and (PP2-Pie) (not (PP-Pie)) (FR-R2) (not (RC)) ))

	(:action Lift-E
		:precondition (and (PP-Pie) (RC) (sFolded))
		:effect (and (PP2-Pie) (not (PP-Pie)) (FR-RC) (not (RC)) ))

	(:action FoldOnTable-F
		:precondition (and (PP-Pie) (RC) (sFolded))
		:effect (and (Pie) (not (PP-Pie)) (I) (not (RC)) ))

	(:action Lift-B
		:precondition (and (PP-Pie) (RC) (Crumpled))
		:effect (and (PP2-Pie) (not (PP-Pie)) (LC-RC) (not (RC)) ))

	(:action PlaceFlatOnTable-B
		:precondition (and (PP2) (LC-RC) (Flat))
		:effect (and (PP2-Pie) (not (PP2)) ))

)