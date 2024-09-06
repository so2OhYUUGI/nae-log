// src/types/FieldCardTypes.ts
export type FieldCardProps = {
	fieldName: string;
	camera: boolean;
	temperature: number;
	humidity: number;
	powerStatus: [boolean, boolean, boolean];
};
