from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentDetails
from .serializers import StudentDetailsSerializer

# @api_view(['GET', 'POST'])
# def student_details_list(request):
#     if request.method == 'GET':
#         students = StudentDetails.objects.all()
#         serializer = StudentDetailsSerializer(students, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = StudentDetailsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def student_details_list(request):
    if request.method == 'GET':
        students = StudentDetails.objects.all()
        serializer = StudentDetailsSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Extract admission_no from request data
        admission_no = request.data.get('admission_no')
        
        # Check if a student with the same admission_no already exists
        if StudentDetails.objects.filter(admission_no=admission_no).exists():
            return Response({'error': 'Student with this admission number already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate and save the new student details
        serializer = StudentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_challan_by_roll_no(request, roll_no):
    try:
        student = StudentDetails.objects.get(entry_no=roll_no)
        serializer = StudentDetailsSerializer(student)
        return Response(serializer.data)
    except StudentDetails.DoesNotExist:
        return Response({'error': 'Student with this roll number does not exist.'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def student_details_list(request):
    try:
        students = StudentDetails.objects.all()
        serializer = StudentDetailsSerializer(students, many=True)  # Pass many=True for a list of objects
        return Response(serializer.data)
    except StudentDetails.DoesNotExist:
        return Response({'error': 'No students found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def update_student_details(request, roll_no):
    try:
        students = StudentDetails.objects.filter(entry_no=roll_no)
        if not students.exists():
            return Response({'error': 'Student with this roll number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        for student in students:
            serializer = StudentDetailsSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'All student details updated successfully.'}, status=status.HTTP_200_OK)
    except StudentDetails.DoesNotExist:
        return Response({'error': 'Student with this roll number does not exist.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_student_by_roll_no(request, roll_no):
    try:
        student = StudentDetails.objects.get(entry_no=roll_no)
        student.delete()
        return Response({'success': 'Student deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except StudentDetails.DoesNotExist:
        return Response({'error': 'Student with this roll number does not exist.'}, status=status.HTTP_404_NOT_FOUND)