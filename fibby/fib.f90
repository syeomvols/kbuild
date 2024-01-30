

        SUBROUTINE FIB(N,A)
      implicit none
      INTEGER, intent(IN):: N
      INTEGER:: i
      REAL(8), intent(OUT):: A(N)
      DO i=1,N
         IF (i.EQ.1) THEN
            A(i) = 0.0D0
         ELSEIF (I.EQ.2) THEN
            A(i) = 1.0D0
         ELSE 
            A(i) = A(i-1) + A(i-2)
         ENDIF
      ENDDO
        END SUBROUTINE
