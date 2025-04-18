@login_required
def search_violators(request):
    """
    API endpoint to search for violators with the same first/last name for the adjudication page
    Returns matching violations in JSON format
    """
    first_name = request.GET.get('first_name', '').strip()
    last_name = request.GET.get('last_name', '').strip()
    current_violation_id = request.GET.get('current_violation', 0)
    
    if not first_name and not last_name:
        return JsonResponse({
            'success': False,
            'message': 'Please provide at least a first name or last name to search',
            'violations': []
        })
    
    # Build query to search for violations with matching violator names
    query = Q()
    if first_name:
        query &= Q(violator__first_name__icontains=first_name)
    if last_name:
        query &= Q(violator__last_name__icontains=last_name)
    
    # Get all violations with the matching name, excluding the current violation
    # Only include violations in PENDING status for batch adjudication
    violations = Violation.objects.filter(
        query,
        status='PENDING'
    ).exclude(id=current_violation_id).select_related('violator', 'enforcer')
    
    # Format the results for JSON response
    results = []
    for violation in violations:
        # Format the violation date for display
        violation_date = violation.violation_date.strftime('%b %d, %Y') if violation.violation_date else 'N/A'
        
        # Get a list of violation types using the proper method
        violation_types = violation.get_violation_types()
        
        # Format the violation data
        formatted_violation = {
            'id': violation.id,
            'violation_date': violation_date,
            'violation_type': violation.violation_type,
            'violation_types': violation_types,
            'status': violation.status,
            'status_display': violation.get_status_display(),
            'fine_amount': str(violation.fine_amount),
            'violator_name': f"{violation.violator.first_name} {violation.violator.last_name}",
            'location': violation.location,
            'enforcer_name': violation.enforcer.get_full_name() if violation.enforcer else 'N/A'
        }
        results.append(formatted_violation)
    
    return JsonResponse({
        'success': True,
        'message': f"Found {len(results)} violations",
        'violations': results
    }) 
